# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division

"""
Find the value of n ≤ 1,000,000 for which n/φ(n) is a maximum.
"""

from factorization import primefactorize, totient
def problem69():
    """
    in fact, it can be solved by print 2*3*5*7*11*13*17=510510  by the set union, theory! smartest way
    """
    ratio=2.0 # 
    pos=2
    N=10**6
    for d in range(3,N+1):
        count=totient(d)
        r=float(d)/count
        if r>ratio: 
            ratio=r
            pos=d
    #
    print("maximum ratio is found at n=:",pos)
    
if __name__ == "__main__":
    #test()
    problem69()