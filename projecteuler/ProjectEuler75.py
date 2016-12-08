# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 75
weblink:
description:



It turns out that 12 cm is the smallest length of wire that can be bent to form an integer sided right angle triangle in exactly one way, but there are many more examples.

12 cm: (3,4,5)
24 cm: (6,8,10)
30 cm: (5,12,13)
36 cm: (9,12,15)
40 cm: (8,15,17)
48 cm: (12,16,20)

In contrast, some lengths of wire, like 20 cm, cannot be bent to form an integer sided right angle triangle, and other lengths allow more than one solution to be found; for example, using 120 cm it is possible to form exactly three different integer sided right angle triangles.

120 cm: (30,40,50), (20,48,52), (24,45,51)

Given that L is the length of the wire, for how many values of
L <=1,500,000 can exactly one integer sided right angle triangle be formed?


Analysis

"""

from projecteulerhelper import *
#timeit is encluded into projecteulerhelper now


# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 


def test():
    # assert
    print(rightangletriangles(120))
    print(rightangletriangles(12)) # 


def rightangletriangles(i):
    """genearate all the possible right angle triangles with integer edge
    for the given integer perimeter i
    list of tuple: [(longest, secondlong, shortest), ..] 
    """
    lmin=int(i/(1+2**0.5))
    lmax=int(i/2)
    lt=[]
    for l in range(lmin, lmax):
        #
        for s in range( int((i-l)/(2**0.5)) ,l):
            t=i-l-s
            if l*l==s*s+t*t:
                lt.append((l,s,t))
        #
    if lt: print(i,lt)
    return lt

def bruteforce():
    """ for each integer find the numbers of triangle, if >1, 
    bruteforce is not possible for big L, 
    """
    L=1500
    c=0
    for i in range(12, L+1):
        if i%2==0 and len(rightangletriangles(i) )== 1:
            c+=1
    print(c)

def smarter():
    """  should not be prime, all  i%2==0
    if %12=0, must have one, 
    """
    pass
    
def solve():
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    test()
    timeit(solve)
    #timeit(func, param)