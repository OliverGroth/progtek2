"""
Solutions to exam tasks for modul 1
Name:
Code:
"""

import random
import time
import math


def count_all(lst, d):
    # basfall
    if lst == []:
        return 0
    # rekursion
    if type(lst[0]) == list: # För att gå djupare i lista
        return count_all(lst[0],d) + count_all(lst[1:],d)
    elif lst[0] == d:
        return 1 + count_all(lst[1:],d)
    else:
        return 0 + count_all(lst[1:],d)


def c(n):
    if n <= 2:
        return 1
    else:
        return c(n-1) - c(n-3)


def c_mem(n):
    memory = {1:1,2:1}

    def _c_mem(n):
        if n <= 2:
            return 1
        else:
            if n not in memory:
                memory[n] = _c_mem(n-1) - _c_mem(n-3)
        return memory[n]

    return _c_mem(n)

    # c_mem(100) = 984549

def main():
    """
    print('Test count_all')
    print(count_all([], 1))
    print(count_all([1, 2, 1, 3, [[1], [1, 2, 3]]], 1))
    
    print('\nTest of c')
    print('c(3):', c(3))
    print('c(4):', c(4))
    print('c(5):', c(5))
    print('c(9):', c(9))

    print('\nTest of c_mem')
    print('c_mem(3):', c_mem(3))
    print('c_mem(4):', c_mem(4))
    print('c_mem(5):', c_mem(5))
    print('c_mem(9):', c_mem(9))

    print('c_mem(100):', c_mem(100))
    """
    #print('\nCode for task B1')

    tests = [31,32,34,35,36,37,38,39,40]
    times = []
    for test in tests:
        start = time.time()
        c(test)
        end = time.time()
        times.append(end-start)

    for i in range(1,len(times)):
        print(times[i]/times[i-1])

    print(times)

if __name__ == "__main__":
    main()
    print('Over and out')


"""
Answer to task B1:




"""
