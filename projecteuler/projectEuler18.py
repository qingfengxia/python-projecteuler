# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
""" http://projecteuler.net/index.php?section=problems&id=18  triangle 
it has been finished in 10 minutes
using recursive method is prefered, brute force  not feasible to solve this problem
"""

from projecteulerhelper import *

#########################################
    
def ProjectEuler18():
    tri = ReadMat('ProjectEuler18.txt', ' ')
    N = len(tri)
    ms=FindMaxSum(tri, 0, 0, N)
    print(ms)

def FindMaxSum(tri,  row, col,n):  
    """ row, col is the start index of trianle"""
    #list=[]
    if n==1: return tri[row][col]
    return tri[row][col] + max( FindMaxSum(tri,  row+1, col,n-1),  FindMaxSum(tri,  row+1, col+1,n-1) )

    
if __name__ == "__main__":
    ProjectEuler18()