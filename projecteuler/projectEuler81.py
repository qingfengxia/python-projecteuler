# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
P81

In the 5 by 5 matrix below, the minimal path sum 
from the top left to the bottom right, 
by only moving to the right and down, 
is indicated in bold red and is equal to 2427.

	
131	673	234	103	18
201	96	342	965	150
630	803	746	422	111
537	699	497	121	956
805	732	524	37	331
	

Find the minimal path sum, in matrix.txt (right click and 'Save Link/Target As...'), a 31K text file containing a 80 by 80 matrix, from the top left to the bottom right by only moving right and down.

"""

""" TSP travelling salesman problem,    traverse all cities once and return,  see wikipedia
    CPP  Chinese postman problem,    travsere all edges once
    
"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

def lineparse(l):
    v=l.strip().split(",")   # line end is included in l
    return [int(s) for  s in v]

   
filename="ProjectEuler81matrixpath.txt"
mat=parseinputfile(filename, lineparse)

def test():
    # assert
    pass

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def bruteforce():
    print(" brute force is not possible for 80X80 matrix ")
    
def smarter():
    """ possible grid move path is the simple problem for this
    using recursive, but it is limited by stack size
    using matrix partition seems reasonable!
    """
    pass
    
def problem81():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem81)
    #timeit(func, param)