# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
#!/usr/bin/python
"""
problem 91
weblink:http://projecteuler.net/problem=91
description:

see webpage

Analysis:
method 1:
    one point must be (0,0)
    recursive  RC(1)=3
    symmetric,  X-axis, Y-axis,  45degree except one case  (n,0),(0,n)
    some special cases,  the right angle is not in (0,0)
    
method 2 bruteforce: 
    still consider the symmetric property
    50**4
    generate combination of coord, then test them!
"""
#from __future__ import *
from projecteulerhelper import *
#timeit is encluded into projecteulerhelper now


# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

def isRightTriangle(x,y):
    #based on the third point at z=(0,0)
    #if x[0]==y[1] and x[0]==0: return True
    #if y[0]==x[1] and y[0]==0: return True
    # more general judgement!
    e2l=sorted([x[1]*x[1]+x[0]*x[0],  y[1]*y[1]+y[0]*y[0],  (y[1]-x[1])**2+(y[0]-x[0])**2  ])
    if min(e2l)==0: return False   # points should be distinct!
    if e2l[2]==e2l[1]+e2l[0]:         return True
    else: return False
    

#~ def countSpecialRightTriangles(n):
    #~ """ second point at (i,n) top edge(coord y=0),   for i in range(1,n), i.e. 
    #~ the two boundaries is not (0,n),(n,n) is not tested here!
    #~ the third point is not on X axis, 
    #~ by bruteforce search
    #~ """
    #~ count=0
    #~ for i in range(1,n):
        #~ for y0 in range(1,n):   #  in fact ,only point below, ZX need to be tested
            #~ for y1 in range(1,n):
                #~ if isRightTriangle((i,n),(y0,y1)): count+=1
    #~ return count
    
#~ def RC(n):
    #~ """ it is easy to make error to distinguish special and regular
    #~ this method is not correct!"""
    #~ if n==1:
        #~ return 3
    #~ else:
        #~ sym=(n-1)*2+1  
        #~ #new ones with point: x(0,n)->n-1,  symX2,   but (0,n)+y(n,0)->1
        #~ #for 0<i<n ,   x(i,n)-> 2,  non-square grid thus 2 on one side,     symX2 for both side of 45degree
        #~ sym+=(n-1)*2*2+2  # p1(n,n),  sym  of 45degree  p2 (0,n)/(n,0)
        #~ tilt=0
        #~ if n%2==0: tilt+=2  # one edge is axis, third point on 45degree 
        #~ special=2*countSpecialRightTriangles(n)  #sym for 
        #~ return RC(n-1)+sym+special+tilt

        
def countAppendedRightTriangles(n):
    """ second point at (i,n) top edge(coord y=0),   for i in range(0,n+1), i.e. 
    the two boundaries points are included: (0,n),
    right end should be treated as special(n,n) , counted once
    third can be point anywhere, but should not be coincident!
    it is nearly bruteforce search
    This method is not  correct!!!,   16870  why?   
    Q point, should not included point on right boundary line (n,?), which is sym, 
    """
    count=0
    for i in range(0,n):   # how to excluded coincident triangle, only one!  for X=(0,n) and Y=(n,0)?
        for q0 in range(0,n):   #  in fact ,only point below, ZX need to be tested
            for q1 in range(0,n+1):
                if isRightTriangle((i,n),(q0,q1)): count+=1
    count*=2  #sym
    count-=1 #X(0,n) Y(n,0) is coincident, must remove once!
    #second point at (n,n), only 2 triangle
    for q0 in range(0,n+1):   #
        for q1 in range(0,n+1):
            if isRightTriangle((n,n),(q0,q1)): count+=1
    return count

def RTC(n):
    if n==1:
        return 3
    else:
        return RTC(n-1)+countAppendedRightTriangles(n)
        
def bruteforce():
    """  it is possible for N=50, but why the number is doubled? 28468
    symmetrical  P and Q , should be divided by two!
    """
    N=50
    print("bruteforce find right triangles for N=",N)
    count=0
    for x1 in range(0,N+1):
        for x2 in range(0,N+1):
            for y1 in range(0,N+1):
                for y2 in range(0,N+1):
                    if isRightTriangle((x1,y1),(x2,y2)): count+=1
    print(count/2)
        
def smarter():
    """
    """
    print(RTC(50))

def test():
    # assert
    print(isRightTriangle((0,5),(12,0)))
    for i in range(2,5): print(i,"=>",RTC(i))
    
def solve():
    #bruteforce()  #correctly
    smarter()
    
if __name__ == "__main__":
    test()
    timeit(solve)
    #timeit(func, param)