# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 43 description:

The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    d2d3d4=406 is divisible by 2
    d3d4d5=063 is divisible by 3
    d4d5d6=635 is divisible by 5
    d5d6d7=357 is divisible by 7
    d6d7d8=572 is divisible by 11
    d7d8d9=728 is divisible by 13
    d8d9d10=289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.


weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#
import itertools  

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def test():
    print([str(i) for i in range(10)]) # just as a list of int, not list of str
    print(pandigital()[1])
    assert "testsubstring(1406357289)==True "


def testsubstring(x):
    p=[2,3,5,7,11,13,17]
    s=str(x)
    for i in range(7):
        if not int(s[1+i:4+i])%p[i]==0:
            return False
    print(s)
    return True
    
def bruteforce():
    #
    pd=pandigital()
    l=[]
    for x in pd:
        if testsubstring(x):
            l.append(x)
    print('Find the sum of all 0 to 9 pandigital numbers with this property: ')
    print(sum(l))   # 16695334890
    
def problem():
    test()
    bruteforce()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)