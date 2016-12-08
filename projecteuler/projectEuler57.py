# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 57
weblink:
description:

It is possible to show that the square root of two can be expressed as an infinite continued fraction.

sqrt(2) = 1 + 1/(2 + 1/(2 + 1/(2 + ... ))) = 1.414213...

By expanding this for the first four iterations, we get:

1 + 1/2 = 3/2 = 1.5
1 + 1/(2 + 1/2) = 7/5 = 1.4
1 + 1/(2 + 1/(2 + 1/2)) = 17/12 = 1.41666...
1 + 1/(2 + 1/(2 + 1/(2 + 1/2))) = 41/29 = 1.41379...

The next three expansions are 99/70, 239/169, and 577/408, but the eighth expansion, 1393/985, is the first example where the number of digits in the numerator exceeds the number of digits in the denominator.

In the first one-thousand expansions, how many fractions contain a numerator with more digits than denominator?


Analysis

"""
from __future__ import division  # // integer division
from factorization import gcd
from projecteulerhelper import *
#timeit is encluded into projecteulerhelper now


# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 



def test():
    # assert
    print(simplify(36,96))
    print(fit(1393,985))
    print('test pass')

def simplify(n,d):
    """ the most simplified fraction form 
    """
    g=gcd(n,d)
    return (n//g,d//g)
    
def fit(n,d):
    #n,d=simplify(n,d)      # if simplification , 153    
    if len(str(n))>len(str(d)):       # if not simplification 153
    #if set(str(n))>set(str(d)):  
        return True
    else:
        return False
        
def bruteforce():
    """ but this form the calc of next item depends on previous one
    calc the numerator and denominitor tuple until 1000th
    if each item is minused by one, it is 1/2, 2/5, 5/12, 12/29, 29/70
    from second item, there is a rule to generate the next one
    """
    N=1000
    tl=[(1,2),(2,5)]
    for i in range(2,N):
        n=tl[i-1][1]
        d=tl[i-1][1]*2+tl[i-1][0]
        if i<10: print(n+d, d)        # debug info
        tl.append((n,d))
    # add 1 to fraction, simplify and count!
    print("len of tl: %d and last pair"%len(tl), tl[-1])
    print("The count for ", sum( [fit(n+d,d) for n,d in tl ] ))

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