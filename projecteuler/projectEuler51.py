# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

By replacing the 1st digit of *3,
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. 
Consequently 56003, being the first member of this family, is the smallest prime with this property.

Find the smallest prime which, by replacing part of the number (not necessarily adjacent digits) 
with the same digit, is part of an eight prime value family.

weblink:

Answer: 

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#
from prime import *
from itertools import combinations
# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def index_tuple_list(ndigits):
    l=[]
    indices=range(ndigits)
    for n in range(1,ndigits):
        l+=[ t for t in combinations(indices, n) ] #
    return l
 
def permutatedigits(string,indextuple,digits):
    l=[]
    threshold=10**(len(string)-1)
    s=list(string)  # str is immutable -> change to list before assign
    for d in digits:
        # if 0 in t and d==0: continue      # or filter the return list
        for i in indextuple:
            s[i]=d
        l.append(int(''.join(s)))
    return [i for i in l if i>threshold]
    # remove the int that the leading zero lead to less total digits, which is not valid
    
def f(x):
    l=[1]
    s=str(x)
    d=[str(i) for i in range(10)]  # is zero valid?
    #change n digits at indices position! generate index list
    for t in index_tuple_list(len(s)):
        xx=list(permutatedigits(s,t,d))
        c= [i for i in xx if isprime(i)] 
        if  len(c)>=8:
            print(x,c)        #120383 [121313, 222323, 323333, 424343, 525353, 626363, 828383, 929393]
        l.append(   len(c) )
    return max(l)

def test():
    print(index_tuple_list(4))
    print(permutatedigits('123456',(0,3),[str(i) for i in range(10)]))
    print(f(13))
    print('end of test')
    
def bruteforce():
    # by increase N, it takes 1 minute to finish the searching
    N=10**6
    for x in primesbelow(N):
        if f(x)>=8:
            break
    
def smarter():
    pass
    
def problem():
    test()
    bruteforce() #take 25second to finish
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)