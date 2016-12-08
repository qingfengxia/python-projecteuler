# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

We shall say that an n-digit number is pandigital 
if it makes use of all the digits 1 to n exactly once;
for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 X 186 = 7254, 
containing multiplicand, multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity
can be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way 
so be sure to only include it once in your sum.



weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

N=9
d=set( [str(i) for i in range(1,N+1) ])

from itertools import permutations

def t2int(t):
    return int(''.join(t))         #how to merge an list/iter?

def test():
    print(d)
    print(t2int(tuple(d)))
    print(d-set(['1','2']))
    
def bruteforce():
    #the product can only be 4  digits number?!
    l=[]
    for tp in permutations(d,4):
        p=t2int(tp)
        for tm in permutations(d-set(tp),2):
            m=t2int(tm)
            ml=[t2int(tc) for tc in permutations(d-set(tp)-set(tm),3)]
            if any([p==m*i for i in ml]):
                l.append(p)
        for tm in permutations(d-set(tp),1):
            m=t2int(tm)
            ml=[t2int(tc) for tc in permutations(d-set(tp)-set(tm),4)]
            if any([p==m*i for i in ml]):
                l.append(p)
    s=set(l)
    print(l)
    print('compared the len of set and list:',len(s), len(l))  # 6->4, should be same len!
    print('sum of all products:', sum(s))  #,  wrong for the first time, 

def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)