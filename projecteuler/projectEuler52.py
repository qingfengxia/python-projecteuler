# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 52
weblink:
description:


It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.


Analysis     
(1) bruteforce

(2) optimization problem,  equation 
"""

from projecteulerhelper import *
#timeit is encluded into projecteulerhelper now


# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 


def test():
    # assert
    fit(125874)
    fit(1552625)
    print(set(str(125874) ))
    assert set(str(125874) ) == set(str(125874*2) )
    

def fit(i):
    dlist=sorted([c for c in str(i)])
    #print dlist
    for j in range(2,7):
        if dlist!=sorted([c for c in str(i*j)]):
            return False
    return True
        
def bruteforce():
    """
    digits (0-9, may be repeating),  search from 3digits ->  n
    x must be 1yyyyyy, less than 17yyyy,then 6x has the same digit length, 
    last digits should not be zeros, 
    """
    n=1
    Nmax=8
    while n<Nmax:
        n+=1
        i=10**n
        imax=int(1.66667*i)
        print("test digit number:",n+1)
        while i<imax:
            i+=1
            dset=set(str(i))
            for j in range(2,7):    #first stage filtering
                if set(str(j*i) ) != dset:
                    continue
            #if all has same digits, but they may have different repeating digits
            #comparison of sorted list?  second stage filtering
            if fit(i):
                print("Find such min positive int:", i) #correct
                print([i*k for k in range(1,6)])
                exit(0)
        

def smarter():
    """ as bruteforce can solve it less than 1 second, no need for smarter 
    """
    pass
    
def solve():
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    test()
    timeit(solve)
    #timeit(func, param)