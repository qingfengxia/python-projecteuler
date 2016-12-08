# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1**4 + 6**4 + 34 + 44
    8208 = 84 + 24 + 04 + 84
    9474 = 94 + 44 + 74 + 44

As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.


weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def f(x,np):
    s=str(x)
    if x==sum([int(s[i])**np for i in range(len(s)) ]):
        return True
    else:
        return False

def test():
    print(f(1634,4))
    
def bruteforce():
    #
    np=5
    max=5*10**np # how to estimate this ??
    start=2 # 1 is always true, do not include it
    l=[i for i in range(start,max) if f(i,np)]
    print(l)
    print(sum( l )) #443839
    

def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)