# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 39 description:

If p is the perimeter of a right angle triangle with integral length sides, {a,b,c}, there are exactly three solutions for p = 120.

{20,48,52}, {24,45,51}, {30,40,50}

For which value of p is no more than 1000, is the number of solutions maximised?


weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

from math import sqrt

def f(p):
    c=0
    for z in range(int(p/(1+sqrt(2))), int(p/2)+1):    #the range of longest edge
        for x in range(1, int(z/sqrt(2))+1):        #the angle can be infered from selection of z
            y=(p-z-x)
            if z*z==x*x+y*y: c+=1
    return c
        

def test():
    print(f(120))
    
def bruteforce():
    start=120  #usually the bigger perimeter has more chance
    m=3
    mp=120
    for p in range(120,1000+1):
        fp=f(p)
        if fp>m:
            mp=p
            m=fp
    print(m,mp)
        

def smarter():
    # sin(theta)+cos(thera)=z/(p-z), therefore theta can be estimated, then x  and y are estimated !
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)