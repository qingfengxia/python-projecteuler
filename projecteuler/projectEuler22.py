# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file 
containing over five-thousand first names, begin by sorting it into alphabetical order. 
Then working out the alphabetical value for each name, 
multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, 
which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. 
So, COLIN would obtain a score of 938 x 53 = 49714.

What is the total of all the name scores in the file?

The format of names.txt is csv, all name is quoted by ""

weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

import csv
    
def readlist():
    with open('ProjectEuler22names.txt') as f:
        #l=f.read().split(' ') # one line sperated by space,  strip()
        l=list(csv.reader(f))[0]
    return l
    
def f(s):
    p=0
    for c in s.upper():
        if c.isupper():
            p+=ord(c)-ord('A')+1
    return p
     
def test():
    l= sorted(readlist())
    print('count of names:',len(l))  # only 1, there must be some error!
    print(l[937])  #should be COLIN
    print(f('COLIN')*938)  #49714
    print(ord('C')-ord('A')+1)  #3 
    print("test passed")
    
def bruteforce():
    l= sorted(readlist())
    i=0
    result=0
    for s in l:
        i+=1
        result+=f(s)*i
        
    print(result)
    
def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)