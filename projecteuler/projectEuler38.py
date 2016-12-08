# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

Take the number 192 and multiply it by each of 1, 2, and 3:

    192 X 1 = 192
    192 X 2 = 384
    192 X 3 = 576

By concatenating each product we get the 1 to 9 pandigital, 192384576. 
We will call 192384576 the concatenated product of 192 and (1,2,3)

The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4, and 5, 
giving the pandigital, 918273645, which is the concatenated product of 9 and (1,2,3,4,5).

What is the largest 1 to 9 pandigital 9-digit number 
that can be formed as the concatenated product of an integer with (1,2, ... , n) where n > 1?


weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

    
def f(l,x):
    r=0
    #pandigital=set([ str(i) for i in range(1,10)])
    s=''.join([str(i*x) for i in l])
    #print s
    #print set(s)
    if len(s)==9 and len(set(s))==9 and ( not'0' in set(s) ):
        print(l,x,s)
        return int(s)
    else:
        return 0
        
def test():
    print(f(range(1,10),1))
    print(f([1, 2, 3, 4, 5], 9))
    
def bruteforce():
    #
    l=[]
    for n in range(2,6):
        stop=10**(6-n)      # this is the key to reduce computation time
        l+=[f(range(1,n+1),x) for x in range(2,stop) ]
    print(max(l))

def smarter():
    pass
    
def problem():
    #test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)