# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
""" problem 
the longest recurring number of 1/d for d<1000
"""
N=1000
def recur(i):
    s=([])
    r1=10%i   #0.xy
    while  not r1 in s:   # it is very slow for in test!
        s.append(r1)  
        r1=(r1*10)%i
    #print i,s
    return len(s)
   
def recur_fast(i):
    #if isprime(i):
    #    return 1
    s=i*[None]
    r1=10%i   #0.xy
    s[0]=r1
    for j in range(1,i):
        r1=(r1*10)%i
        s[j]=r1
    #print i,s
    return len(set(s))
    
lmax=1
imax=1
for i in range(5,N): # 1-999
    li=recur_fast(i)
    if li>lmax:
        lmax=li
        imax=i
    print(i,li)
print(lmax,imax)  #982 983 
# is that the max prime lower than 1000?
    