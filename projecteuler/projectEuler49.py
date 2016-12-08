# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

The arithmetic sequence, 1487, 4817, 8147, in which each of the terms increases by 3330,
is unusual in two ways: 
(i) each of the three terms are prime, and, 
(ii) each of the 4-digit numbers are permutations of one another.

There are no arithmetic sequences made up of three 1-, 2-, or 3-digit primes, 
exhibiting this property, but there is one other 4-digit increasing sequence.

What 12-digit number do you form by concatenating the three terms in this sequence?


weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def test():
    pass
    
def bruteforce():
    #
    from prime import primesbelow
    #from math import abs
    ps=set([i for i in primesbelow(10000) if i>1000]) # it must be a 4 digits numbers
    #set is not sorted, even the input is sorted
    print('total primes with exact 4 digits:',len(ps))
    for x in ps:
        #
        s=str(x)
        if len(set(s[:-1]))==3 and  not ('0' in set(s) ):
            x1=int(s[1]+s[2]+s[0]+s[3]) 
            if x1 in ps:
                x2=int(s[2]+s[0]+s[1]+s[3])
                if x2 in ps and abs(x1-x)==abs(x2-x1):
                    print(sorted([x,x1,x2]))
    

def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)