# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
#!/usr/bin/python
#What is the greatest product of four adjacent numbers 
#in any direction (up, down, left, right, or diagonally) in the 20*20 grid?

from projecteulerhelper import *

def ProjectEuler11():
     """  how to read the space seperated 2D matrix in python
     using cvs and array module,  List of Lists    numpy.array()"""
     fileName = "ProjectEuler11.txt"
     table = ReadMat( fileName,' ')
     maxm = 1
     ns = 4  # four consectutive
     N = len(table)
     print(table[0])   #test the mat reading
     for row in range(N-ns):
         for col in range(N-ns):
             ret=MaxConsecutive(table, row,col,ns)
             maxm = max( ret, maxm)
     print(maxm)
    
def MaxConsecutive(ll, row,col,ns):
    """ find out the max square of the consectutive n numbers  """
    maxn = 1
    maxc=max(  [ MultipleN(ll[row+i][col:col+ns-1])    for i in range(ns) ]  )
    maxr=max(   [ MultipleN( [ ll[row+j][col+i]  for j in range(ns) ])   for i in range(ns) ]  ) # slicing fail? 
    # will ll[row:row+ns-1][col+i]) return a list?
    diag1=1
    diag2=1
    for i in range(ns):
        diag1=diag1*ll[row+i][col+i]
        diag2=diag2*ll[row+ns-1-i][col+i]
    return max([maxc, maxr, diag1, diag2])  
     
def MultipleN(list):
    s=1
    for i in range(len(list)):
        s=s*list[i]
    return s

if __name__ == "__main__":
    ProjectEuler11()


    