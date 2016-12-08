# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

In the hexadecimal number system numbers are represented using 16 different digits:
0,1,2,3,4,5,6,7,8,9,A,B,C,D,E,F

The hexadecimal number AF when written in the decimal number system equals 10x16+15=175.

In the 3-digit hexadecimal numbers 10A, 1A0, A10, and A01 the digits 0,1 and A are all present.
Like numbers written in base ten we write hexadecimal numbers without leading zeroes.

How many hexadecimal numbers containing at most sixteen hexadecimal digits exist 
with all of the digits 0,1, and A present at least once?

Give your answer as a hexadecimal number.
(A,B,C,D,E and F in upper case, without any leading or trailing code that marks the number as hexadecimal and without leading zeroes ,
e.g. 1A3F and not: 1a3f and not 0x1a3f and not $1A3F and not #1A3F and not 0000001A3F)


weblink:

Analysis:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#
from math import factorial

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def P(N,s):
    if N<s: return 0
    r=1
    for i in range(s):
        r*=(N-i)
    return r
 
def C(N,s):
    if N<s: return 0
    r=1
    for i in range(s):
        r*=(N-i)
    return r/factorial(s)
    
def f(N):
    """ permutates '01A' by factorial(3), choose N-3 places from N =>production 
    exclude the cases: zero is at the first position, permutates '1A' by factorial(2), choose N-3 places from N-1 =>production 
    """
    #return   ( C(N,3) * factorial(3) - C(N-1,2) * factorial(2) ) * 16**(N-3)   #CF593F4E531A7124  error!s
    #return   (  factorial(3) - factorial(2) ) * 16**(N-3)  # all 4  error!
    return    2* P(N-1,2)  * 16**(N-3)  + (16-3)*P(N-1,3) * 16**(N-4) 
    
def test():
    print(C(5,3))
    print(f(3))
    print(f(4))
    print(f(5))
    print('test passed')
    
def bruteforce():
    print('{0:X}'.format(sum( [ f(i) for i in range(4,17) ]) + 4))   
        
def smarter():
    """
    http://blog.dreamshire.com/2009/04/09/project-euler-problem-162-solution/
    """
    s = 0
    for n in range(3, 17): 
        p=15 * 16**(n - 1) + 41 * 14**(n - 1) - (43 * 15**(n - 1) + 13**n)
        print(n,p)
        s+=p
    print("Answer to PE162 = %X" % s)
    
def problem():
    test()
    bruteforce()
    smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)