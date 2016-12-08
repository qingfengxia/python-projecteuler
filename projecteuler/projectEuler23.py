# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, 
which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and
it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 

By mathematical analysis, it can be shown that all integers greater than 28123 
can be written as the sum of two abundant numbers. 

However, this upper limit cannot be reduced any further by analysis 
even though it is known that the greatest number that cannot be expressed 
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.

weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
from math import sqrt

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 


def d(n):
    s = 1
    t = sqrt(n)
    for i in range(2, int(t)+1):
        if n % i == 0: s += i + n / i
    if t == int(t):
        s -= t
    return s
 
def test():
    pass
    
def bruteforce():
    limit = 28123   #  other guy use 20162 as upper limit ,why?
    s = 0
    abn = set()
    for n in range(1, limit):
        if d(n) > n:
            abn.add(n)
        if not any( (n-a in abn) for a in abn ):
            s += n
    print("sum of all the positive integers of such: ", s)

def smarter():
    pass
    
def problem():
    #test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)