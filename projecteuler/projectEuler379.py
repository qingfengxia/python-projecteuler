# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

Let f(n) be the number of couples (x,y) with x and y positive integers, x <= y 
and the least common multiple of x and y equal to n.

Let g be the summatory function of f, i.e.: g(n) = sum of f(i) for 1 <= i <= n.

You are given that g(10**6) = 37429395.

Find g(10**12).


weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

from factorization import lcm

def f(n):
    #bruteforce
    l=[]
    for y in range(1,n):
        l.append( len([ (x,y)   for x in range(1,y+1) if lcm(x,y)==n]) )
    return sum(l)
    
def g(n):
    return sum([f(i) for i in range(1,n+1)])

def test():
    #
    print(f(10))
    print(g(10**6)) # even this can not be solved by bruteforce
    print('end of test()')
    
def bruteforce():
    #
    pass

def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)