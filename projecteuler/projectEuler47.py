# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

The first two consecutive numbers to have two distinct prime factors are:

14 = 2 x7
15 = 3 x 5

The first three consecutive numbers to have three distinct prime factors are:

644 = 2**2 x 7 x 23
645 = 3 x 5 x 43
646 = 2 x 17 x 19.

Find the first four consecutive integers to have four distinct primes factors. What is the first of these numbers?


weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#
from factorization import primefactorize as primefactors
# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 


def f(c):
    #c=4
    if c==3:
        start=10**2
        stop=10**3
    else:
        start=10**1
        stop=10**6   #  it take 43 seconds to finish this search, 
        
    l=[(x,len(set(primefactors(x)))) for x in range(start, stop)]
    for i in range(len(l)-c+1):
        if all(ci[1]==c for ci in l[i:i+c]):
            print(l[i:i+c])         #134043
            break
    
def bruteforce():
    #
    f(4)

def test():
    print(primefactors(7))
    print(primefactors(644)) # there is repeated primes in such list, 
    print(primefactors(645))
    print(primefactors(646))
    f(3)
    print("end of test")

def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)