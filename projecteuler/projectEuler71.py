"""
Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, 
it is called a reduced proper fraction.
If we list the set of reduced proper fractions for d <=8 in ascending order of size, we get:
1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that 2/5 is the fraction immediately to the left of 3/7.
By listing the set of reduced proper fractions for d <=1,000,000 in ascending order of size, 
find the numerator of the fraction immediately to the left of 3/7.
#########################################
428571.0 / 1000000 -> 0.428571
428570.0 / 999997 -> 0.428571285714
428523.0 / 999887 -> 0.428571428571

#although the answer given by projecteuler is 428570, I doubt! 
#I am not sure my hasCommonFactor(n,d) is correct!? 
"""
    
from __future__ import print_function, unicode_literals, absolute_import, division
from projecteulerhelper import *
import math
import prime
from factorization import primefactorize, gcd    # only apply to a number less than 1 million

def problem71():

    #the prime near N,  
    N=10**6
    ratio= 0.4
    pos=0
    """
    #try only primer denumerator, 
    pl=prime.primesbelow(N)
    l=len(pl)
    for i in range(1, l-4):
        r=math.floor(pl[l-i]*(3/7.0)) / float(pl[l-i])
        if r>ratio:
            ratio=r
            pos=pl[l-i]
    """
    #try all denumerator from 8 until N
    #from factorization import gcd
    for d in range(N, 7,-1):
        n=math.floor(d*(3/7.0)) 
        r=n/ float(d)
        if r>ratio and (gcd(n,d)):
            print(n, "/",d, "->",r)
            ratio=r
            pos=d
    print("try to solve problem 71")
    print(pos, ratio, pos*ratio)
    # 

if __name__ == "__main__":
    timeit(problem71)