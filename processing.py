import multiprocessing as mp
import math
import os
import time


def process_info():
    print('Module:' + str(__name__) + '\n')
    print('Parent Process id:' + str(os.getppid()) + '\n')
    print('Process id:' + str(os.getpid()) + '\n\n')


def cubes_and_sqare_root(a):
    # process_info()
    return (int(a), math.sqrt(a ** 3))


def main():
    pool = mp.Pool(processes=mp.cpu_count())

    s = time.clock()
    results = [pool.map(cubes_and_sqare_root, (x for x in range(1, 10000000)))]
    e = time.clock()

    print(e - s)


if __name__ == '__main__':
    main()

