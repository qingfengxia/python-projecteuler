# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
http://projecteuler.net/problem=53

There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general,

nCr =	n! /( r!(n-r)! )
,where r  n, n! = n(n1)...321, and 0! = 1.
It is not until n = 23, that a value exceeds one-million: 23C10 = 1144066.

How many, not necessarily distinct, values of  nCr, for 1  n  100, are greater than one-million?
"""
# 503 is not correct,   it can use more than ten digits

#try to calc all that is less than M,  f(M),  then find the all the possible combination of r and n

#~ def factorial(n):
#~    p=1
    #~ if n>=1:     
        #~ for i in (range(1,n+1)):
            #~ p=p*i
    #elif n==0:
        #return 1 
    #else:  raise ValueError("  factorial is not edfined for minus integer")
        
from math import factorial

def combinations_count(choices, selections):
    if n>=r:     return factorial(choices)/factorial(selections)/factorial(choices-selections)
    else:    raise ValueError("choices is less than selections")
    
def ncr(n,r):
    if n>=r:     return factorial(n)/factorial(r)/factorial(n-r)
    else:    raise ValueError("first param n less than r")
    
def test():
    print("factorial(10)=",factorial(10))
    print("factorial(0)=",factorial(0))
    print("ncr(23,10)=1144066? ",  ncr(23,10))
    print("ncr(8,1)=? ",  ncr(8,1))   #8 

N=100
M=10**6

# not include zero, nC0?   it is tricky to calc the MaxCombinations
# all the valid combination is triangle, not square:
MaxCombinations=(N*N-N)/2+N

#brute force, not very slow, 0.2second
def method1():
    d=0
    for i in range(1, N+1):
        for j in range(1,i+1):
            if ncr(i,j)>M:
                #print i,
                d=d+1

    print("The combination higher than ", d)

################## method 2,easy to run into error #######################
def method2():
    c=0
    v=0
    for i in range(1, N+1):
        v=v+i
        for j in range(1,i+1):
            if ncr(i,j)<=M:
                #print i,
                c=c+1   
            else:
                #print i, j
                # should not break directly. as the j increase, ncr() can drops, it is not unidirectional
                c=c+j  # ncr()  is symmetry  for  n and n-r 
                break  

    #correctly, why? it 
    print("less than that number, count=", c)
    print("MaxCombinations=",MaxCombinations, "=?", v)
    print(MaxCombinations-c)


if __name__ == "__main__":
    method1()
