# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

A googol (10**100) is a massive number: one followed by one-hundred zeros; 
100**100 is almost unimaginably large: one followed by two-hundred zeros. Despite their size, the sum of the digits in each number is only 1.

Considering natural numbers of the form, ab, where a, b < 100, what is the maximum digital sum?


weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def test():
    #
    print('end of test()')
    
def bruteforce():
    #
    l=[ ]
    for a in range(2,100):   # a or b =1 or 100 need not be tested
        for b in range(2,100):
            l.append(str(a**b) )
    print((max([ sum([int(c) for c in s]) for s in l])))   #972  correct  at the first trial

def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)