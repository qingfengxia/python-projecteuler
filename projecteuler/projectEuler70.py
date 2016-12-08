# -*- coding: utf-8 -*-

"""

Euler's Totient function, φ(n) [sometimes called the phi function], is used to determine the number of positive numbers less than or equal to n which are relatively prime to n. For example, as 1, 2, 4, 5, 7, and 8, are all less than nine and relatively prime to nine, φ(9)=6.
The number 1 is considered to be relatively prime to every positive number, so φ(1)=1.

Interestingly, φ(87109)=79180, and it can be seen that 87109 is a permutation of 79180.

Find the value of n, 1 < n < 10**7, for which φ(n) is a permutation of n and the ratio n/φ(n) produces a minimum.

"""
from __future__ import print_function, unicode_literals, absolute_import, division

from factorization import primefactorize, totient
from prime import isprime
import itertools

def test():
    assert totient(87109)==79180
    #print(list(itertools.permutations(str(31))))
    assert set(str(13)) == set(str(31))

def phi(n):
    """ if it is prime number, n/phi(n) is small near 1
    but for prime number  phi(n)=n-1, 
    
    """
    if isprime(n):
        return n-1
    else:
        s=[]
        #to-do
        return len(s)

def problem70():
    print("try to solve problem 70 by bruteforce")
    l = []
    min = 1
    for i in range(2,10**6):
        phi_i = totient(i)
        if not phi_i/i < min:
            continue
        else:
            if set(str(i)) == set(str(phi_i)):
                l.append((i,phi_i/i))
                min = phi_i/i
    ll = sorted(l, key=lambda t:t[1])
    print(ll[0][0])
    
    
if __name__ == "__main__":
    test()
    problem70()