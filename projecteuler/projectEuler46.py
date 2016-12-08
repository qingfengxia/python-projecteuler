# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

It was proposed by Christian Goldbach that every odd composite number 
can be written as the sum of a prime and twice a square.

9 = 7 + 2x1**2


It turns out that the conjecture was false.

What is the smallest odd composite that cannot be written as the sum of a prime and twice a square?


weblink:

Answer: 5777  correct for the first time

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

d=['1','3','5','7','9']

import math
from prime import isprime

def t(x):
    stop=int(math.sqrt(x/2.0))
    for i in range(0,stop+1):         #test the square from 0,
        if isprime(x-2*i*i):
            return True
    return False
    
def f(n):
    from itertools import product
    l=[ i for i in tuple_iter_to_int_list(product(d,repeat=n) ) if t(i)==False ]
    return l

def test():
    print(t(9))
    
def bruteforce():
    for n in range(2,6):  #n digits
        fl=f(n)
        if len(fl)>0:
            print(min(fl))   #5777  correct for the first time
            break
            
def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)