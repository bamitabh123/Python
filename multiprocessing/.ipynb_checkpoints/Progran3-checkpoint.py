from multiprocessing import Pool
import time

def f(x):
    print( x*x)

if __name__ == '__main__':
    pool = Pool(processes=4)
    pool.map(f, range(10))
    r = pool.map_async(f, range(10))
    # DO STUFF
    print( 'HERE')
    print( 'MORE')
    r.wait()
    print( 'DONE')
