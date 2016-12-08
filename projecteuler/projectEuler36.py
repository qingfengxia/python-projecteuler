# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

The decimal number, 585 = 1001001001 (binary), is palindromic in both bases.

for n<10 ?  for 22 2442?

Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

(Please note that the palindromic number, in either base, may not include leading zeros.)

weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def f(x):
    r=False
    if str(x) == str(x)[-1::-1]:
        b='{0:b}'.format(x)
        if b == b[-1::-1]:
            r=True
    return r

def test():
    print(f(1))
    print(f(3))
    print(f(585))

def bruteforce():
    #
    N=10**6
    print(sum([i for i in range(1,N) if f(i)]))  #872187
        

def smarter():
    # permutation
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)