# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

Euler published the remarkable quadratic formula:

(n*n) + n + 41

It turns out that the formula will produce 40 primes for the consecutive values n = 0 to 39. 
However, when n = 40, 40**2 + 40 + 41 = 40(40 + 1) + 41 is divisible by 41, 
and certainly when n = 41, 41**2 + 41 + 41 is clearly divisible by 41.

Using computers, the incredible formula  n*n - 79n + 1601 was discovered, 
which produces 80 primes for the consecutive values n = 0 to 79. 
The product of the coefficients, -79 and 1601, is -126479.

Considering quadratics of the form:

    n*n + a*n + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |-4| = 4

Find the product of the coefficients, a and b, 
for the quadratic expression that produces the maximum number of primes for consecutive values of n, starting with n = 0.

weblink:

"""

from projecteulerhelper import *
from prime import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def test():
    print([n*n+n+41  for n in range(40)])
    
def bruteforce():
    """ Analysis:  b must be postive prime under 1000,  since n begin with zero
    """
    N=1000
    M=1
    ab=(1,41)
    # n*n + a*n + b, fitting the curve to get the a,   n=0 and n=1
    l=primesbelow(N*5)
    print(len(l),l[-1])
    for i in range(10,N):  # when to end the test?
        b=l[i]
        if b>=N:
            break
        # search upward
        n=1
        a=(l[i+n]-b-n*n)/n  #b=l[i] for n=0
        while l[i+n]==n*n+n*a+b:
            n+=1
        if n>M:  
            M=n
            ab=(a,b)
            print(n,ab)
        # search downward
        n=-1
        a=(l[i+n]-b-n*n)/n  #b=l[i] for n=0
        while l[i+n]==n*n+n*a+b:
            n-=1
        if -n>M:  
            M=-n
            ab=(a,b)
            print(n,ab)
    (ax,bx)=ab
    print(ab, ax*bx)
    
def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)