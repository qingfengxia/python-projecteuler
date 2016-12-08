# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
import itertools
import math
from projecteulerhelper import *

def CountOfCircularPrimesBelowN(N):
    """ problem 35
    The number, 197, is called a circular prime
    because all rotations of the digits: 197, 971, and 719, are themselves prime.
    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
    How many circular primes are there below one million?
    """
    #N=1000000
    from prime import isprime
    Digits= int( math.log10(N) ) 
    print(Digits ,"digits number should be tested beblow" ,N)
    # method 1
    count = 4 # all 1 digits, 
    result = set([2,3,5,7])
    for e in range(2,Digits+1):
        for i in range(10**e + 1, 10**(e+1)):
            if( isprime(i)):            
                #test all circularNo(i,e)
                ul = circularNo(i)
                # has filtered the same number ->set(list)
                if( all([isprime(v) for v in ul])  ):
                    count = count + len(ul)
                    result = result & ul
                    #continue is suggest in this context
    #there should be a lot of repeated number, need to filter out
    # just stop this method,   too slow to find answer
    print(" count of circuler number bellow:", N,"is :", count)   

def method2(N):
    # method 2:  prime test for permutation with repeated (product)of digits [1 3 7 9]
    #  if get the  combination with repeated ->   definitely you will miss some out, circular number is not full permutations
    #  Error use the combinations:  N=10000  -> 26 (?), but N=1000000  -> 26 
    # all primes has more than 1 digits :  must be combination: 1 3 7 9,
    # take care of the number with all same digits: 111  3333, 
    # do NOT care the circular number, just the combination of 1 3 7 9 
    # N=100-> 13, correct; 
    from prime import isprime
    nDigits= int( math.log10(N) )
    print(nDigits ,"digits number beblow" ,N)
    count = 4 # all number have 1 digits, 
    if(nDigits == 1):
        print(" count of circuler number bellow:", N,"is :", count)
        return 
    dlist = ['1','3','7','9']
    s = set([2,3,5,7])
    for e in range(2,nDigits+1):
        #intL=tuple_list_to_int_list(combinations_with_replacement(dlist,e) )
        intL=tuple_list_to_int_list(itertools.product(dlist,repeat=e) )
        st = set()
        for i in set(intL):
            ul = circularNo(i)
            #print ul
            if all(isprime(i) for i in ul):
                count = count + len(ul) # there may be identical number already in list
                st=st | ul
        s =s | st
    print(" count of circuler number bellow:", N,"is :", len(s)) 
    print(s)



def main():
    #timeit is import from helper, instead of timeit module
    
    #timeit(CountOfCircularPrimesBelowN)
    #dir(itertools)  # does not work in script?
    print(circularNo(139779))
    #
    N=1000000 #0000
    #CountOfCircularPrimesBelowN(N)
    #print tuple_list_to_int_list(combinations_with_replacement('1379',6) )
    timeit(method2, N)
    #CountOfCircularPrimesBelowN(N)
    
    # str -> tuple  eval('(1, 2, 3, 4, 5)')
    # concat tuple to str 
    #wait=raw_input("wait any key to eixt")
    
if __name__ == "__main__":
    main()
    
    """  Threading on the project euler
    1) Get the single digit ones directly.
    2) We know that the numbers have to end in 1,3,7,9 (except for the single digit ones). Also, all primes are of the form
    6n-1 or 6n+1. Therefore, given an ending digit and the reminder when divided by 6, we can find all the possible ending digits that can be prime in a decade. For example, if you divide 11 by 6, it gives a reminder of 5. This means, than 11 is of the form 6n-1. Therefore, possible primes are 11,13,17,19. I leave it upto the reader to figure out the other possibilities.
    3) Once you have seen a sequence with a given first digit, you never have to use that digit again for a given number of digits in a number. For example, for 2 digit numbers, once you have finished 11 to 19, you never have to use 1 again because you have seen all 2 digit numbers that contain a 1 and can possibly be prime.

    Here is the python code that does this all.

    from Primes import *
    # Stores the possible last digits of primes in a given decade given the reminder
    # of the first number in the decade when divided by 6
    pattern = {5: [1,3,7,9], 1: [1,7], 3: [3,9]}
    # ES is the eratostenes sieve upto 1000. Running it upto 1000000 takes for ever.
    # So just do until a number that makes sense. Any larger numbers, use the
    # number in es to figure out if the are prime.
    es = ES(10000)

    #IsPrime() finds out if a number is prime. I have not included the code here.

    def FillCircPrimes(n, left, digits, found):
    assert left > 0
    def Fill(n, found, check):
    if found.has_key(n):
    return
    f = []
    s = str(n)
    for i in range(len(s)):
    if check:
    check = IsPrime(n, es)
    f.append(n)
    s = s[1:] + s[:1]
    n = int(s)
    for i in f:
    found = check

    n = n * 10
    if left==1:
    d = pattern[(n+1)%6]
    for i in digits:
    Fill(n+i, found, i in d)
    return

    left = left - 1
    for i in digits:
    FillCircPrimes(n+i, left, digits, found)

    def FindCircPrimes(nDigits):
    from time import time
    s = time()
    found = {2:True, 3:True, 5:True, 7:True}
    for d in range(2, nDigits+1):
    digits = [1,3,7,9]
    for i in range(len(digits)):
    FillCircPrimes(0, d, digits, found)
    digits.pop()
    r = [n for n,b in found.items() if b]
    r.sort()
    t = (time() - s)*1000
    return r,t

    Runs < 400ms on my P3@450. 
    Can be optimized more with more known things but did not feel it was worth in.
    """