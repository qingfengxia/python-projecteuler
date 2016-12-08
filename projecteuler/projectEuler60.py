# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 109, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

----------analysis: 

[3, 7, 109, 673]  is the first fourth, the fifth should be higher than 673. 

weblink:

"""
from __future__ import print_function
from projecteulerhelper import *
from prime import *
#timeit is import from helper, instead of timeit module

# test the correction by a small dimension first. 
# test  brute force first, method1

#then, try some smart method! 

def test():
    assert allprime(3,[7, 109, 673]) == True
    
def allprime(p,s):
    for i in s:
        if not  isprime( int(str(p)+str(i) ) )  or not  isprime( int(str(i)+str(p) ) ):
            return False
    return True

def brute_force():
    # brute force not possible, 
    N=int(1e6)
    l=primesbelow(N)
    s=[3, 7, 109, 673] #, 673
    for i in l:
        if allprime(i,s):
            s.append(i)
            print("the appended prime is ", i)
            print("hte sum of primes is ", sum(s))
            return
    print("failed to find the prime under", N)            

def problem():
    brute_force()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)