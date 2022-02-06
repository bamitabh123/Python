import subprocess
import traceback
import datetime
import time
import os
import logging
import csv

# Create and configure logger
logging.basicConfig(filename="newfile.log",
                    format='%(asctime)s %(message)s',
                    level=logging.INFO,  # Only INFO and lower level
                    filemode='w')

# Creating an object
logger = logging.getLogger()


# Setting the threshold of logger to DEBUG
# logger.setLevel(logging.DEBUG)


def printBeginBanner(msg):
    logger.info("/")
    logger.info("############################################################################")
    logger.info(" %s " % msg)
    logger.info("############################################################################")
    logger.info("//")


def printEndBanner(status):
    logger.info("/")
    logger.info("############################################################################")
    logger.info(" Status: {%s} " % ("PASS" if status == 0 else "FAIL"))
    logger.info("############################################################################")
    logger.info("//")


def setupLogDir(LOGBASE):
    print("Setting Up LogDir for logging ...")
    timestamp = datetime.fromtimestamp(time.time()).strftime('%Y%m%d')
    logdir = os.path.join(os.path.abspath(os.sep), LOGBASE, timestamp)
    if not os.path.exists(logdir):
        os.makedirs(logdir)
    return logdir


def setupLogger(logdir, logfile_basename):
    print("Setting up logger...")
    timestamp = datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H.%M.%S')
    logFormatter = logging.Formatter("%(asctime)s.%(msecs)03d %(levelname)s %(module)s - %(funcName)s: %(message)s")
    rootLogger = logging.getLogger()
    rootLogger.setLevel(logging.INFO)
    FileHandler = logging.FileHandler("{0}/{1}.{2}.log" .format(logdir, logfile_basename, timestamp))
    rootLogger.addHandler(logFormatter)
    rootLogger.addHandler(FileHandler)

    return rootLogger



##############################
## Run Commands in Parallel ##
##############################


def runCommandInParallel(commandList, maxProcs, shellFlag=True):
    logger.info("Running command")
    processes = []
    status = 0
    maxProcs = int(maxProcs)
    for cmd in commandList:
        try:
            if len(processes) == maxProcs:
                logger.info("Max process limit [%d] reached!" % maxProcs)
                processes, newStatus = waitForAnyProcessToComplete(processes)
                status += newStatus
            if len(processes) == 1:
                time.sleep(2)
            logger.info("Starting process with PID : [%s] " % cmd)
            proc = subprocess.Popen(cmd, shell=shellFlag, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
            res = proc.communicate()
            logger.info("Process started with PID : [%d] " % proc.pid)
            if proc.returncode != 0:
                # print("res =", res)
                logger.error("ERROR: = [%s]" % (res[1].decode().strip('\n')))

            processes.append(proc)
        except Exception as e:
            status += 1
            logger.error("Error occurred while running process! [%s]" % cmd)

    status += waitForRemainingProcesses(processes)
    return status


def waitForAnyProcessToComplete(runningProcs):
    status = 0
    startingCount = len(runningProcs)
    logger.info("Waiting for any process to complete...")

    while len(runningProcs) == startingCount:
        for proc in runningProcs:
            retcode = proc.poll()
            if retcode is not None:
                logger.info("Process [PID:%d] returned with status : [%d] " % (proc.pid, retcode))
                status += retcode
                logger.info("Removing completed process ...")
                runningProcs.remove(proc)
                logger.info("Running process count [%d] " % len(runningProcs))
                # canReturn = True
                break
        time.sleep(.5)
    return runningProcs, status


def waitForRemainingProcesses(processes):
    status = 0
    logger.info("Waiting for [%d] running processes to complete..." % len(processes))
    while len(processes) > 0:
        for proc in processes:
            retcode = proc.poll()
            if retcode is not None:
                logger.error("Process [PID:%d] returned with status : [%d] " % (proc.pid, retcode))
                status += retcode
                processes.remove(proc)
                break
        time.sleep(1)
    return status
