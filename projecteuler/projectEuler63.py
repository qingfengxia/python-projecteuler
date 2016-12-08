# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 63
weblink:
description:


The 5-digit number, 16807=7**5, is also a fifth power. 
Similarly, the 9-digit number, 134217728=8**9, is a ninth power.

How many n-digit positive integers exist which are also an nth power?


"""

from projecteulerhelper import *
#timeit is encluded into projecteulerhelper now


# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 


def test():
    # assert
    pass

def bruteforce():
    """ Analysis:  should be easy to bruteforce, 
    since the upper limit of n is:  9**n<10*(n-1)
    Note: 1-9 is included already 
    """
    l=[i for i in range(1,10)]
    Nmax=30
    for n in range(2,Nmax+1):
        imax=10
        #print "%d digit test unti imax="%n, imax
        for i in  range(1,imax):
            if len(str(i**n)) == n:
                l.append(i**n)
                print(i, i**n)
    print("Result:",len(l))
        

def smarter():
    """
    """
    pass
    
def solve():
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    test()
    timeit(solve)
    #timeit(func, param)