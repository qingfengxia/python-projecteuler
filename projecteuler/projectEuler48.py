# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
10digit surpass the int32 
"""
    
def ProjectEuler48():
    print(str(sum([i**i for i in range(1,1000)]))[-10:])
    #sum = 10405071317 #first 10

def SumPower(M,x,n):
    """(M+x)^n = sum(), M must be multiple of 10 
    This method is not suitable for n>20""" 
    NumberOfDigits =10
    s = 0
    for i in range(0, NumberOfDigits): #0->9
        s = s + Comb(n,i)*(x**(n-i))*(M**i)
        
#global var for faster access to 
c=[0]*10
f=[0]*10

def Comb(n,k):
    """ k=0, return 1, k=1, return n
    """
    ret =1
    for i in range(1,k): ret=ret*(n-i)
    return ret/Factorial(k)
        
def Factorial(k):  #can be put into a array predined, 
    s=1
    for i in range(2,k+1): s=s*i              #when k=0, it does not report error, correct!
    return s

#######################################
def BruteForce(n): 
    limit = n
    sum = 0
    for i in range(1, limit+1):
        if(i%10 != 0):
            sum = sum + pow(i,i)
    sumStr = str(sum)[-10:]
    print(sumStr)

if __name__ == "__main__":
    print(str(sum([i**i for i in range(1,1000)]))[-10:])   # 1000^1000 is not needed!
    # python above line only 0.3second is finished!
    
    #BruteForce(1000)  # it only takes 1.7s to finish!!   9110846700      # not using the unlimited precision but longlong int C++ ()