# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""  P34
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
    Note: as 1! = 1 and 2! = 2 are not sums they are not included.
    Problem: Find the sum of all numbers which are equal to the sum of the factorial of their digits.
"""
from projecteulerhelper import *

from math import factorial
fl=[ factorial(i) for i in range(10)]  #: the first one, 0!==1 will not be used!
    
def f(n):
    s=0
    d=n 
    while d>0:
        s+=fl[d%10]
        d =d//10
    return s

def ProjectEuler34():
    """   
    using table lookup instead of doing facterial() 
    since 9! = 362880,  so it must be a 6 digits or less
    """
    NMAX=sum(fl)
    i=3
    s=0
    while i<NMAX:
        if i ==  f(i):
            s+=i
        i+=1
    print("um of all numbers i.e. sum of the factorial of their digits:", s)
        
def test():
    print(fl)
    assert 59//10==5 and  59%10==9
    assert fl[59%10]==fl[9]
    print(f(145))
    assert f(145)==145

if __name__ == "__main__":
    test()
    timeit(ProjectEuler34) 