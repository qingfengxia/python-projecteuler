# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division

""" Work out the first ten digits of
    the sum of the following one-hundred 50-digit numbers.
"""
    
from projecteulerhelper import *

##########################################
def ProjectEuler13():

    # read them into a int matrix ,  50-digit numbers is divided into 10 5digits number
    # int32 can only hold 9digits number 
    fileName = "ProjectEuler13.txt"
    nd=5
    ll=ReadBigInt(fileName, nd)
    print("the row of data file, count of big int", len(ll))
    SumMultipleDigits(ll,nd)
    
def SumMultipleDigits(ll,nd):
    """ sum of multiple digits >>int32, each number is put in a row list """
    s=[]
    sumStr='' #make sure it is NOT same name with funciton sum!!!
    base=10
    for col in range(len(ll[0])):
        s.append(  sum([ll[row][col]    for row in  range(len(ll)) ])   )
    for i in range(len(ll[0])-2, -1, -1):
        s[i] += int(s[i+1]/(base**nd))
        s[i+1] = s[i+1] % (base**nd)
    for col in range(len(ll[0])):    # when you copy code, MUST replace sth!!!
        sumStr += str(s[col])
    print("the first ten digits", sumStr[:10])
    return sumStr
    
if __name__ == "__main__":
    ProjectEuler13()
