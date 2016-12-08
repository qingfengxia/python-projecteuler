# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division

"""
problem 14 description:

Longest Collatz sequence

weblink: 
https://projecteuler.net/problem=14

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def chain(x):
    c=1
    while x>1:
        if x%2==0: 
            x=x/2
        else: 
            x=x*3+1
        c+=1
    return c
 

def test():
    # 
    print(chain(13))
    
def bruteforce():
    #
    #brute force, it seems  possible
    N=10**6
    cmax=1
    imax=1
    for i in range(N,N//3, -1):
        ci=chain(i)
        if ci>cmax:
            cmax=ci
            imax=i
    print('the start number: ', imax, ' which produce the longest chain of ' ,cmax)

def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)