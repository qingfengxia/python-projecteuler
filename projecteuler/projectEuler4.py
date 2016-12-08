# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 * 99.

Find the largest palindrome made from the product of two 3-digit numbers.

weblink:

"""


from projecteulerhelper import *
#timeit is import from helper, instead of timeit module

# test the correction by a small dimension first. 
# test  brute force first, method1

#then, try some smart method! 


def test():
    assert max_palindromic_number(2)==9009

def max_palindromic_number(ndigits):
    l=[]
    for i in range(10**ndigits-1,10**(ndigits-1),-1):
        for j in range(10**ndigits-1,10**(ndigits-1),-1):
            if str(i*j)==str(i*j)[::-1]: #
                #print i,j,i*j
                l.append(i*j)
                break
    return max(l)

def problem():
    print((max_palindromic_number(3)))
    
if __name__ == "__main__":
    test()
    timeit(problem)
    #timeit(func, param)