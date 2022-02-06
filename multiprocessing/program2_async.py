import multiprocessing
import time


def square(x):
    if x ==2:
        time.sleep(20)
        return x * x
    if x ==3:
        time.sleep(30)
        return x * x
    return x*x

if __name__ == '__main__':
    pool = multiprocessing.Pool()
    inputs = [0,1,2,3,4]
    outputs_async = pool.map_async(square, inputs)
    outputs1 = outputs_async.successful()
    outputs = outputs_async.get()
    print("Output1: {}".format(outputs1))
    print("Output: {}".format(outputs))