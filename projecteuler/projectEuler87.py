# -*- coding: utf-8 -*-

"""
problem 87
weblink:
description:

The smallest number expressible as the sum of a prime square, prime cube, and prime fourth power is 28. In fact, there are exactly four numbers below fifty that can be expressed in such a way:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

How many numbers below fifty million can be expressed as the sum of a prime square, prime cube, and prime fourth power?


Analysis

"""

from __future__ import print_function, unicode_literals, absolute_import, division
from projecteulerhelper import *
#timeit is encluded into projecteulerhelper now
from prime import isprime,primesbelow

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 


def test():
    # assert
    pass

def bruteforce():
    """ bruteforce seems not possible
    """
    N=5*10**7
    l=set()
    l2=[i**2 for i in primesbelow(int(N**0.5))]
    l3=[i**3 for i in primesbelow(int(N**(1.0/3.0)))]
    l4=[i**4 for i in primesbelow(int(N**0.25))]
    print(l2,l3)
    for i4 in l4:
        for i3 in l3:
            for i2 in l2:
                isum=i2+i3+i4
                if isum <= N:
                    l.add(isum)
                else:
                    break
    print(len(l))

def smarter():
    """
    """
    pass
    
def solve():
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    test()
    timeit(solve)
    #timeit(func, param)