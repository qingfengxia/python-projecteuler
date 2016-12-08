# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n exactly once. 
    For example, 2143 is a 4-digit pandigital and is also prime.
What is the largest n-digit pandigital prime that exists?
"""

digits="123456789"
from prime import isprime
from itertools import permutations


from tuple_list_to_int_list import tuple_list_to_int_list

for i in range(9,3,-1):
    l=[ j  for j in tuple_list_to_int_list(permutations(digits[:i])) if isprime(j) ]
    #print i, l
    if any (l): 
        print("largest n-digit pandigital prime ",max(l))      
        break
    
    