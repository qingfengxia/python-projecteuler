# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
from projecteulerhelper import *

def print_spiral(N):
    """
    Problem 28, method 1 stupid print out the spiral matrix, but practice of matrix indexing sense
    """
    #declear a matrix of NXN
    s=[[0]*N for x in range(N)]
    assert(N%2 == 1)
    
    cen = int(math.floor(N/2))  # python nth ele put in [n-1]
    layers = int(math.floor(N/2))
    s[cen][cen]=1
    for layer in range(1,layers+1):
        length = layer*2 + 1  #ele len of the square
        radius = layer
        # loop the square from         s[cen-radius+1][cen+radius]  to s[cen-radius][cen+radius]
        s[cen-radius+1][cen+radius] = s[cen-radius+1][cen+radius-1] + 1  #index error?
        for index in range(2, length): # right edge, clockwise 
            s[cen-radius+index][cen+radius] = s[cen-radius+index-1][cen+radius] + 1
        for index in range(1, length): # bottom edge, clockwise 
            s[cen+radius][cen+radius-index] = s[cen+radius][cen+radius-index+1] + 1
        for index in range(1, length): # left edge from bottom corner, clockwise 
            s[cen+radius-index][cen-radius] = s[cen+radius-index+1][cen-radius] + 1
        for index in range(1, length): # ceil edge, clockwise 
            s[cen-radius][cen-radius+index] = s[cen-radius][cen-radius+index-1] + 1
    print("print the spiral", N, "X", N)
    for i in range(N):
        print(s[i][:])
        #for j in range(N):
            #print  "%4i"%s[i][j]  # it will automatically print a new line!
            # import sys
            # sys.stdout.write(" ")
            # using pprint.pprint 
    #for big N print into a file , with speical format!
        
def sum_diagnonals_spiral(N):
    """
    Problem 28, method 2 , serial:  1:1, 3:45, 5:101
    spiral 5X5 has 1+4*2+4*4 25 element, max element is 25, ele size N*N
    the upper right corner number must the N*N, the other 3 corners counter-clockwise by -(N-1)
    """
    # 
    s=1 # spiral 1
    for l in range(3,N+2,2):
        s=s+l*l  
        s=s+l*l-(l-1)
        s=s+l*l-2*(l-1)
        s=s+l*l-3*(l-1)
    print("sum of the all diag number of spriral", N, "is: ", s)
    return s
    
def main():
    #timeit is import from helper, instead of timeit module
    timeit(sum_diagnonals_spiral,1001)
    wait=raw_input("wait any key to eixt")
    
if __name__ == "__main__":
    main()