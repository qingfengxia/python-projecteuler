# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
#!/usr/bin/python

"""
problem 72
weblink:
description:

Consider the fraction, n/d, where n and d are positive integers. If n<d and HCF(n,d)=1, it is called a reduced proper fraction.

If we list the set of reduced proper fractions for d <= 8 in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5, 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8

It can be seen that there are 21 elements in this set.

How many elements would be contained in the set of reduced proper fractions for d <=1,000,000

Analysis:
(1)The presumption if n/d is reduced proper fractions, thge  (1-n/d) should also be that, is  correctly!

(2)generate the primelist can improve speed, get the factor list,  
then using set union to get ratio of proper reduced factions, 

(3)method from thread 72
It's basically the sum of the Euler Totients from phi(2) to phi(1000000). 
"""

from projecteulerhelper import *
#timeit is encluded into projecteulerhelper now


# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 
import math
import prime
from factorization import primefactorize, gcd    # only apply to a number less than 1 million

Denumerator=10**3
primelist=prime.primesbelow(Denumerator)  #math.floor(math.sqrt(Denumerator))  should be enough

def hasCommonFactor(n,d):
    """  return False if no common prime factor,  e.g. (1, any positive number>1)
    return  true if faction n/d can  be reduced any more, 
    this function does not do reduction
    d is prime is tested outside!
    """
    return gcd(n,d)!=1
    """
    print gcd(428523, 999887)  == 142841
    print hasCommonFactor(428523, 999887) 
    #    
    minN=min([n,d]) 
    if minN==1:  return False     #  it must be false,  1 is not a prime, 
    if max([n,d])%minN==0:  return True    #counting for the case d==n
    maxf=minN//2     
    for p in primelist:
        if p>maxf: break
        else:  
            if  ((n%p)==0  and (d%p)==0 ):
                return True
    return False
    """
            
def count_bruteforce(d):
    """this is bruteforce method, not possible for big d
    (until 1000   is  310973)   # error ! because hasCommonFactor(n,d) is not proper implemented
    The presumption if n/d is reduced proper fractions, thge  (1-n/d) should also be that, is  correctly!
    if d is even, then 7/14, can be reduced further!
    """
    #if d<=3 and d>1:          return d-1   #test outside!
    count=2  # count for 1/d and (d-1)/d
    for n in range(2,d//2+1):    # if d is odd,  like 15, then 7=(d//2) and 8 all should be counted, 
        if not hasCommonFactor(n,d): 
            count+=2
            #print "%d/%d"%(n,d)
    return count
        
from itertools import combinations
def factorset_union(d):
    """ if the set slist has too much element, to computer the unit
    test by d<=1000, different from bruteforce method!  
    if factorial(list)==d, this should not be counted
    """
    slist=list(set(primefactorize(d)) )# set operation 
    l=len(slist)
    """
    if l==1:  
        u=d/slist[0] 
    if l==2:
        u=(d/slist[0] + d/slist[1]) 
        u-=d/(slist[1]*slist[0])
    if l==3:
        u= (d/slist[0] + d/slist[1] + d/slist[2] ) 
        u-= d/(slist[0]*slist[1]) + d/(slist[1]*slist[2]) + d/(slist[2]*slist[0])
        u+= d/(slist[0]*slist[1]*slist[2])
    #
    """
    u=0
    for i in range(1,l+1):
        u+= (-1)**(i+1)  * sum([ d/reduce(lambda x,y:x*y,c) for c in combinations(slist, i)] )
    return d-u
        
def countProperFaction(d):
    """ for non-prime number, get the list of factor
    proper factions for denumerator no bigger than 1000: 304191   (tested correctly)
    """
    if prime.isprime(d):
         return (d-1)
    else:
        #return count_bruteforce(d)
        return factorset_union(d)

def properFactionUntilN(N):
    """ begin with 1/2, ending with (N-1)/N
    It is proposed that if n/d is reduced proper fractions, thge  (1-n/d) should also be that
    if the denumerator d is a prime, then (d-1)
    """
    count=1  # 1/2  is special 
    for d in range(3,N+1):
        count+=countProperFaction(d)
    return count
   
def bruteforce():
    count=1  # 1/2  is special 
    for d in range(3,N+1):
        if prime.isprime(d):
            count+=d-1
        else:
            count+=count_bruteforce(d)  # error

def smarter():
    """ The time spent on  solve is :  63.5099679207  Second in Python
    """
    print("proper factions for denumerator no bigger than %d"%Denumerator)
    print(properFactionUntilN(Denumerator))
    
def test():
    #
    print("set of primefactorize %d"%10**6)
    print(set(primefactorize(10**6)))
    #
    testset=[4,6,12, 30, 210, 210*11] # must be non prime
    for d in testset: 
        print("test d=%d"%d)
        print(set(primefactorize(d)))
        print(countProperFaction(d))
        print(count_bruteforce(d))
    #print 2*3*5*7*11*13*17*19
    #test count_bruteforce(d) 
    for d in range(3,1001):
        if count_bruteforce(d) != countProperFaction(d):
            print(d, "should be ",countProperFaction(d), " but get",count_bruteforce(d)) 
    #
    assert properFactionUntilN(8)==21

    
def solve():
    #bruteforce()
    smarter()
    
if __name__ == "__main__":
    #test()
    #problem69()
    timeit(solve)
    #timeit(func, param)