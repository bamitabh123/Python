import subprocess
import traceback
import datetime
import logging
import time
import sys
import os
import argparse
import pipes
import tvbase


def parseArguments():
    parse = argparse.ArgumentParser(description="Start Running jobs")
    parse.add_argument("-c", dest="command", required=True, help="job command with fixed input parameter")
    parse.add_argument("-f", dest="filename", required=True, help="Full path of filename containing parameter")
    parse.add_argument("-p", dest="maxproc", required=True, help="Number of parallel jobs")
    args = parse.parse_args()
    print("=====================================================================================================")
    print("Command -->", args.command)
    print("Input Filename -->", args.filename)
    print("Parallel Degree -->", args.maxproc)
    print("=====================================================================================================")
    return args


def checkArguments():
    print("Checking Arguments")
    infoDict = {}

    if os.path.isfile(ARGS.filename):
        file_name = ARGS.filename
    else:
        raise Exception(" %s does not exists ", ARGS.filename)

    if ARGS.maxproc:
        max_proc = ARGS.maxproc
    else:
        max_proc = 1

    if ARGS.command:
        cmd_prefix = ARGS.command
    else:
        raise Exception("Missing Executing command")

    infoDict["filename"] = file_name
    infoDict["max_proc"] = max_proc
    infoDict["cmd_prefix"] = cmd_prefix

    return infoDict


def generateCommands(pfile, cmd_prefix):
    print("Generating commands for files....")
    cmds = []

    for p in open(pfile):
        cmd = cmd_prefix + " " + pipes.quote(p.strip('\n'))
        cmds.append(cmd)
    return cmds


def printCommandList(commandList):
    print("Command:")
    print("{")
    for cmd in commandList:
        print(cmd)
        print("}")


def main():
    global ARGS, LOGDIR, LOGGER, processDate

    ARGS = parseArguments()
    InfoDict = checkArguments()

    processDate = datetime.datetime.fromtimestamp(time.time()).strftime("%Y-%m-%d")

    # BASENAME = os.path.basename(sys.argv[0])
    #
    # LOGBASE = os.path.join(os.path.abspath(os.sep), 'logs', 'app', 'myapplication')

    # LOGDIR =

    # LOGGER

    try:
        tvbase.printBeginBanner("Start running jobs in parallel, degree =" + InfoDict["max_proc"])
        loadcommands = generateCommands(InfoDict["filename"], InfoDict["cmd_prefix"])
        printCommandList(loadcommands)
        status = tvbase.runCommandInParallel(loadcommands, InfoDict["max_proc"])
        tvbase.printEndBanner(status)
        sys.exit(status)

    except Exception as e:
        print(traceback.format_exc())
        sys.exit(1)


if __name__ == "__main__":
    main()
