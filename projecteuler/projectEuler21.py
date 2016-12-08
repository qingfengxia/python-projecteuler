# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

Let d(n) be defined as the sum of proper divisors of n 
(numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a a is not equal to b,
then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are
1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; 
therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; 
so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.

weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def proper_divisors(n):
    limit = int(n ** .5) + 1
    divisors = [1]
    for i in range(2, limit):
        if n%i == 0:
            divisors += [i, n//i]
    return sum(divisors)

d=proper_divisors

def test():
    print('d(284)=',d(284))
    print('d(220)=',d(220))
    assert d(284) == 220
    print('test passed')
    
def bruteforce():
    #
    N=10000
    l=[]
    for i in range(1,N):
        dx=d(i)
        if dx!=i  and  d(dx)==i and dx<N:
            l.append(i)
            #l.append(dx)  # repeated!!!
    print('sum of all the amicable numbers under ',N, 'is ', sum(l))  #31626
        

def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)