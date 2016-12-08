# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 45 description:

Triangle, pentagonal, and hexagonal numbers are generated by the following formulae:
Triangle 	  	Tn=n(n+1)/2 	  	1, 3, 6, 10, 15, ...
Pentagonal 	  	Pn=n(3n-1)/2 	  	1, 5, 12, 22, 35, ...
Hexagonal 	  	Hn=n(2n-1) 	  	1, 6, 15, 28, 45, ...

It can be verified that T285 = P165 = H143 = 40755.

Find the next triangle number that is also pentagonal and hexagonal.


weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#
import itertools

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def T(n): 
    return  n*(n+1)/2 
def P(n): 
    return n*(3*n-1)/2
def H(n): 
    return n*(2*n-1) 

def test():
    assert "T(285) == P(165)"
    assert "H(143) == 40755"
    
def bruteforce():  #possible!
    #
    ih_start=143+1
    ip=165
    it=286
    for ih in itertools.count(ih_start):
        while P(ip)<H(ih):
            ip+=1
        if P(ip)==H(ih) :
            it=2*ih
            print(P(ip))
            break
            
def smarter():
    #using the reverse func of T() P() H()
    #  it=2*ih    
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)