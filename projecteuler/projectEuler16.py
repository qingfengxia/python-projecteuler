# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division

"""
problem description:

2**15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000?

weblink: https://projecteuler.net/problem=16

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def test():
    print(2**50)
    print('0123'[-1])  # 3
    print('0123'[:-1])  # '012'   does not include the last one,  
    print('0123'[:0])    # empty
    
def bruteforce():
    # one liner
    print("solution:", sum([int(c) for c in str(2**1000)[:-1]]))   
    # there is trailing L for python 2.x long type, but python 2.7 str(long) will remove the 
def smarter():
    pass
    
def problem():
    #test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)