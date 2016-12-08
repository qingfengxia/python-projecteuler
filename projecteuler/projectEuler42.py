# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

The nth term of the sequence of triangle numbers is given by, tn = n(n+1)/2; 
so the first ten triangle numbers are:

1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

By converting each letter in a word to a number corresponding to its alphabetical position 
and adding these values we form a word value.
For example, the word value for SKY is 19 + 11 + 25 = 55 = t(10). 
If the word value is a triangle number then we shall call the word a triangle word.

Using words.txt (right click and 'Save Link/Target As...'), 
a 16K text file containing nearly two-thousand common English words, 


how many are triangle words?

weblink:

"""

from projecteulerhelper import *
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

import csv
    
def readlist():
    with open('ProjectEuler42words.txt') as f:
        #l=f.read().split(' ') # one line sperated by comma, double quoted
        l=list(csv.reader(f))[0]
    return l
    
def f(s):
    p=0
    for c in s.upper():
        if c.isupper():
            p+=ord(c)-ord('A')+1
    return p
     
def test():
    print('f(SKY) should be 55' , f('SKY'))
    print(ord('C')-ord('A')+1)  #3 
    
def bruteforce():
    tset=set([i*(i+1)/2 for i in range(40)])  #ten letter word will not exceed 260
    l=readlist()
    print('count of words:',len(l))  
    c=sum([1  for s in l if (f(s) in tset)  ])
    print('count of triangle words:',c)
    
def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)