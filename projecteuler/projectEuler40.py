# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 40
weblink:
description:

An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

Analysis:

"""

from projecteulerhelper import *
#timeit is encluded into projecteulerhelper now
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 


def test():
    # assert
    pass

def bruteforce():
    """ brute force is possible less than 1 second
    """
    i=9
    s="123456789"
    Imax=3*10**5  #  10**6 / 5;  
    while i<Imax:
        i+=1
        s+=str(i)
        
    result=1
    for i in range(7):
        result*=int(s[10**i-1])
    print(result)
        

def smarter():
    """  d_1=1, d_10=1, d_100=5 (10-50:  10th-101th), 
    899-49*2)
    it can be soved by pen
    """
    pass
    
def problem():
    test()
    bruteforce() # 171 second to finish
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)

