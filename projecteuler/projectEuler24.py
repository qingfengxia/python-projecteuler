"""
problem description:

weblink:

A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
"""
 

from projecteulerhelper import *

from itertools import *
from math import *

# test  brute force first, method1
# test the correction by a small dimension first. 

#then, try some smart method! 


N=10
M=10**6

def combinations_count(choices, selections):
    if n>=r:     return factorial(choices)/factorial(selections)/factorial(choices-selections)
    else:    raise ValueError("choices is less than selections")
        
def permutations_count(n):
    if n>=1: return factorial(n)


def test():
    assert "2**2==4"
    print "test passed"

def method1():
    # itertools.permutations()  is in the lexicographic order
    print "total permutation count", permutations_count(N), "  for digits", N
    c=0
    for t in permutations(range(N)):   # the return can not be indexed by [M-1]
        c=c+1
        if c==M: print ''.join(str(list(t)))  #2783915460

#
def method2():
    num=[]
    c=0
    for i in range(1,N):
        print i  #ith element is the first element
        p=permutations_count(N-i)
        for ii, n  in enumerate( set(range(N))-set(num) ):   # set substract , ordered set
            if c+ii*p <= M and c+p*(ii+1) > M:  
                c=c+ii*p
                num.append(n)
        
     
def problem():
    test()
    method1()
    
if __name__ == "__main__":
    print range(1,N)   # range is a list , list substract? 
    print set(range(1,N))
    problem()
    #timeit(func, param) ,     # or using python -c cProfiling.py yourmodulefile.py