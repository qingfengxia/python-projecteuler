# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
#!/usr/bin/python
"""
problem 100
weblink:http://projecteuler.net/problem=100
description:




If a box contains twenty-one coloured discs, composed of fifteen blue discs and six red discs, and two discs were taken at random, it can be seen that the probability of taking two blue discs, P(BB) = (15/21)X(14/20) = 1/2.

The next such arrangement, for which there is exactly 50% chance of taking two blue discs at random, is a box containing eighty-five blue discs and thirty-five red discs.

By finding the first arrangement to contain over 10**12 = 1,000,000,000,000 discs in total, 
determine the number of blue discs that the box would contain.


Analysis:
uint64_t   is enough , so is double precison to get root
(b/t)*(b-1)/(t-1)=1/2
b=(1+math.sqrt(2t*t-2t+1)  )  / 2
# sqrt() result is double?  test again if b is integer!
4*b*b-1==(2t*t-2t+1)



"""
#from __future__ import *
from projecteulerhelper import *
#timeit is encluded into projecteulerhelper now


# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

import math
def f(t):
    """ t*t-t=2(b*b-b), find the integer solution for this function, f(b)"""
    b=0.5*(1+math.sqrt(2*t*t-2*t+1) )
    bp1=int(math.ceil(b))
    bm1=int(math.floor(b))
    if (2*bp1)*(bp1-1)==t*(t-1) or (2*bm1)*(bm1-1)==t*(t-1): 
        print(t,b)
        return (True,b)
    #print t,b,  (2*bp1)**2-1, (2*t*t-2*t+1) # debug
    return (False,b)
    
def test():
    # assert
    f(21)
    f(120)
    for i in range(121,10**3): f(i)

def bruteforce():
    """  if a jump can be calculated, it should be faster 
    b=0.5*(1+math.sqrt(2*(t-0.5)**2+0.5) )
    """
    N=10**12
    testings=1000000
    for i in range(N,N+testings):
        if f(i)[0]:  break
    print("not found by testing number= ",testings)

def smarter():
    """
    """
    pass
    
def solve():
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    test()
    timeit(solve)