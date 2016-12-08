# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
Three distinct points are plotted at random on a Cartesian plane, 
for which -1000 <=x, y <=1000, such that a triangle is formed.

Consider the following two triangles:

A(-340,495), B(-153,-910), C(835,-947)

X(-175,41), Y(-421,-714), Z(574,-645)

It can be verified that triangle ABC contains the origin, whereas triangle XYZ does not.

Using triangles.txt (right click and 'Save Link/Target As...'), a 27K text file containing the co-ordinates of one thousand "random" triangles, find the number of triangles for which the interior contains the origin.

NOTE: The first two examples in the file represent the triangles in the example given above.
-340,495,-153,-910,835,-947
"""

from projecteulerhelper import *

filename="ProjectEuler102triangles.txt"

def test():
    assert containorigin([(-340,495), (-153,-910), (835,-947)])
    assert containorigin([(-175,41), (-421,-714), (574,-645)]) == False
    print("A(-340,495), B(-153,-910), C(835,-947) has origin in triangle! test passed")

def distance(p1,p2, p):
    """ compare distance(point origin to line_P1_P2) and distance(point p to line_P1_P2)
    find the line_P1_P2 cross the axis x0 and y0,   line passing p with a slope of k
    k !=0 k != inf,  catch error and print out for further analysis
    """
    if p2[0]==p1[0] :
        return p[1]-p1[1]
    if p2[0]==p1[0] :
        return p[0]-p1[0]
    # 
    k=(p2[1]-p1[1])/float(p2[0]-p1[0])   # must be float,  float division by zero
    y0=p2[1] - k*p2[0]
    #x0=-y0/k
    y0p=p[1]-k*p[0]
    #return ((x0*y0)/(x0*x0+y0*y0))**2
    if y0*y0p<0:  # different sign, so on both side of origin
        return True
    else:
        return False

def minedge2(plist):
    """ min edge length in polygon, return the square of the edge length
    """
    el2=[]
    for i in range(len(plist)-1):
        e2=(plist[i+1][0]-plist[i][0])**2 + (plist[i+1][1]-plist[i][1])**2
        el2.append(e2)
    e2close=(plist[-1][0]-plist[0][0])**2 + (plist[-1][1]-plist[0][1])**2
    el2.append(e2)
    return min(el2)
    
def containorigin(plist):
    """ find the line cross the axis x0,y0,  
    k !=0 k != inf,  catch error and print out for further analysis
    """
    #minedge=minedge2(plist)
    p1,p2,p3=plist
    return all([distance(p1,p2,p3), distance(p1,p3,p2),distance(p3,p2,p1)])

def method1():
    """ method one:  if line  BC: y=kx+y0, cross y axis at y_BC, line passing A point with slope k cross y-axis at y_A
         y_BC should has opposite sign as y_A,   similar requirement is for  B to AC,   C to AB
         method two: sum of distance to A,B and C, should less than sum the longest two edges
         This is not tested!
    """
    f=open(filename)
    lc=0
    ec=0
    tc=0
    for l in f.readlines():
        v=l.strip().split(",")   # line end is included in l
        #print v
        if len(v)==6:
            lc=lc+1
            a=(int(v[0]), int(v[1]) )
            b=(int(v[2]), int(v[3]) )
            c=(int(v[4]), int(v[5]) )
            if containorigin([a,b,c]):
                tc=tc+1
        else:
            ec=ec+1  # error in parse line
    if ec>0:
        print("error happens in parse line")
    else:
        print("%d triangles has been found with origin inside in %d triangles"%(tc,lc))
        
def problem():
    test()
    method1()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)
