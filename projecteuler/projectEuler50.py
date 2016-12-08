# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
The prime 41, can be written as the sum of six consecutive primes:
41 = 2 + 3 + 5 + 7 + 11 + 13

This is the longest sum of consecutive primes that adds to a prime below one-hundred.

The longest sum of consecutive primes below one-thousand that adds to a prime, contains 21 terms, and is equal to 953.

Which prime, below one-million, can be written as the sum of the most consecutive primes?
"""


from prime import isprime, primesbelow
import math
#reverse searching jump is better!
# jump length is also relative to l[i],   if floor( N/l[i] ) < M: break
# cal N=100 000 first, to increase the M to search, 

#the error first occur, not searching from smallest prime: 2, then ...

#7 543 997651

N=1000000
l=primesbelow(N//10)  #  N/100 is too small,  
print("primes under", N//10, "=", len(l))
M=21  #  contains 21 terms, and is equal to 953
prime=953
for i in range( len(l)):
    if math.floor( N//l[i] ) < M: 
        print("number higher than ", l[i], "is not worth to search")
        break
    for j in range( M, len(l)-M):  #jump of searching of consecutive primes list, 
        s=sum(l[i:i+j])
        if s>N:
            break
        if s<N and j>M and isprime(s):
            print(l[i],j, s)  
            M=j
        #it takes too long time to finish! 
    