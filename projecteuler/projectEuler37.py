# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
import prime

def ProjectEuler37():
    """
    The number 3797 has an interesting property. Being prime itself, 
    it is possible to continuously remove digits from left to right, 
    and remain prime at each stage: 3797, 797, 97, and 7. 
    Similarly we can work from right to left: 3797, 379, 37, and 3.
    Find the sum of the only eleven primes that are both truncatable from left to right and right to left.
    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.
    Solution:  
    1 is not prime, so two digits can only be 37 73 
    then, for number has 3 or more digits, those must be started and ended with 3 or 7
    but the digits between can be combination_with_repeation of [1,3,7,9]
    """
    count =2
    numbers=[37,73, 23, 53] # I miss the first two 23, 35,  filter the 2digits combination of [2 3 5 7]
    MaxDigits = 10
    TotalNo = 11
    for d in range(3,MaxDigits+1):
        # generate a list of possible numbers
        for n in ListOfCandiates(d):
            if( all(prime.isprime(i) for i in ListOfTruncatble(n,d))):
                count = count +1
                numbers.append(n)
                print(n)
            if (len(numbers) == TotalNo): break
        if (len(numbers) == TotalNo): break
    print(numbers)
    print(sum(numbers))
 

import itertools
dl = ['1','3','7','9']
def ListOfCandiates(nDigits):  # this is the bottleneck of the performance
    list = []
    for s in tuple_list_to_int_list(itertools.product(dl,repeat=nDigits-2)):  #return list of tuple
        list.append(int('3'+str(s)+'7'))  # 3*10**(nDigits-1)+s*10+7
        list.append(int('3'+str(s)+'3'))
        list.append(int('7'+str(s)+'7'))
        list.append(int('7'+str(s)+'3'))
    return list

def tuple_list_to_int_list(tl):
    s=[]  #list,  how to declear an empty set?
    for j in tl: 
        # permutations : NO repeated
        number=''
        for c in j :
            number=number+c
        s.append(int(number))
    return s

def ListOfTruncatble(number,nDigits):
	list =[number]
	for i in range(1,nDigits):  # the first and last number has been fixed as 7 or 3
		list.append(number%10**i)
		list.append(number//10**i)
	return list

def IsPrimeTruncatable(n, ndigits):
    if(n>100):
        if( prime.isprime(n) == False): 
            for i in range(2,ndigits):
                if(prime.isprime(n//10**i) == False  or  prime.isprime(n%10**i) == False ): return False
        
if __name__ == "__main__":
	n=7973  # 713 7313  7973 is not prime
	l= ListOfTruncatble(n,len(str(n)))
	print(l)
	result =[37,73, 23, 53, 317,313,373,797,  3137,  3797, 739397]  # 739397 is not good, but it is been added
	if(all([prime.isprime(i) for i in l])): 		print(n, " is  good ")
	if(not prime.isprime(n)): 		print(n, " is  not a prime ")
	print(sum(result))
	ProjectEuler37()