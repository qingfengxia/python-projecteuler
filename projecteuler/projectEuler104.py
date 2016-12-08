# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 104 description:

It turns out that F541, which contains 113 digits, is the first Fibonacci number for which
the last nine digits are 1-9 pandigital (contain all the digits 1 to 9, but not necessarily in order). 
And F2749, which contains 575 digits, is the first Fibonacci number for which 
the first nine digits are 1-9 pandigital.

Given that Fk is the first Fibonacci number for which the first nine digits AND the last nine digits are 1-9 pandigital, find k.

weblink:

"""

from projecteulerhelper import *
from fibonacci  import *
#timeit is import from helper, instead of timeit module

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 
digitset=set([str(i) for i in range(1,10)])

    
def bruteforce(Nstart=2749):
    # brute force is not possible, MAX_N=20000
    MAX_N=Nstart+2000
    F0,F1,N=fib_bigNth(Nstart)
    while N<MAX_N:
        if set(str(F1)[-9:])== digitset  and set(str(F1)[:9])== digitset :
            break;
        else:
            F=F0+F1
            F0=F1
            F1=F
            N=N+1
    
    print("pan digits at head and tail is found at ", N)
    print(str(F1)[-9:], str(F1)[:9])
            

def top_digits(n):
    """  why?
    multiplication by (1+sqrt(5))/2 to track the first 9 digits.
    """
    # t = n * log10(phi)          + log10(1/sqrt(5))
    t = n * 0.20898764024997873 + (-0.3494850021680094)
    t = int((pow(10, t - int(t) + 8)))
    return t
  
def is_pandigital(n):  # input must be 9 digits or less
    if set(str(n))==digitset:
        return True
    else:
        return False
        
def smart():
    """ http://blog.dreamshire.com/2009/06/04/project-euler-problem-104-solution/
    """
    fn, f0, f1 = 2, 1, 1
    while not is_pandigital(f1) or not is_pandigital(top_digits(fn)):
         f0, f1 = f1, (f1+f0)%10**9  # mode 10**9 to truncate the last 10digit
         fn += 1
    print("Answer to PE104 = ", fn)

def test():
    print(digitset)
    print(str(fib_bigNth(541)[0]))   # str(long int ) will strip the last char 'L'
    print(str(fib_bigNth(541)[0])[-9:]) 
    assert set(str(fib_bigNth(541)[0])[-9:])== digitset   # last char is   for long int in python 2.x
    assert set(str(fib_bigNth(2749)[0])[:9])== digitset
    
def problem():
    test()
    #bruteforce()
    smart()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)