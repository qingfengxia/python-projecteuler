# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
P67 max sum of triangle


By starting at the top of the triangle below and moving to adjacent numbers 
on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom in triangle.txt (right click and 'Save Link/Target As...'), a 15K text file containing a triangle with one-hundred rows.

NOTE: This is a much more difficult version of Problem 18. 
It is not possible to try every route to solve this problem, 
as there are 2**99 altogether! If you could check one trillion (10**12) routes every second it would take over twenty billion years to check them all. 
There is an efficient algorithm to solve it. ;o)

"""

from projecteulerhelper import *
from timeit import timeit
#
filename="ProjectEuler67maxsumoftriangle.txt"

def lineparser(l):
    return [int(s) for s in l.strip().split(" ")]
    
    
tri=parseinputfile(filename, lineparser)

def test():
    assert tri[0]==[59]
    print(tri[12])  # 06 -> 6, yes!

def smarter():
    """ (1) nearest neighbour can not give the exact maximum solution
    try to sort each row by decreasing order,     search from bottom which has more chance to get a bigger numbers
    for i,x in enumerate(testlist) 
    
    (2) level set:  all numbers are less than 100,  get some seeds x>nmax*50%
    find the long possible path (threshold nl=50%/2),  
    then increase level, find the longest path
    
    (3) for extreamly large datasheet,  2000X2000, convert them to image and using image analysis
    for each step, calc the complexity by  f(n)
    1) xmax=max(mat), if randomized
    2) 4-level gray scale-> 50% is important, 75%, 25%, debugging by image show! python GUI
    3) path searching -> forking, find the long path
    4) try to interconnect path to mega-path (pixel under threhold is considered)
    5) if mega is less than threhold megepath_threhold (50%-75%), 
    6) go back to step 1) reduce the threshold, but all previous search paths are stored for further extension
    
    other openopt to solve opt:   ant colony optimization (ACO)   Bee Colony Optimization
    drilling problem: d2103 (has 2103 data point)
    """
    pass
    
def problem():
    test()
    smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)