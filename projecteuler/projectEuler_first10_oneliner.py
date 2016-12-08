"""
problem description:

weblink:

"""

from __future__ import print_function, unicode_literals, absolute_import, division
from projecteulerhelper import *

def problem1():
    """
    Problem 1
    If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. 
    The sum of these multiples is 23.
    Find the sum of all the multiples of 3 or 5 below 1000.
    Answer:  233168	
    """
    print("problem1:", sum( set([i for i in range(1,1000) if i%5==0]) | set([i for i in range(1,1000) if i%3==0])) )
    #remove the repeated number, which are  multiples of 3*5=15

def problem3():
    """
    The prime factors of 13195 are 5, 7, 13 and 29.
    What is the largest prime factor of the number 600851475143
    Answer: 	6857
    """
    from factorization import primefactorize
    print("problem3:", max(primefactorize(600851475143)))
    
def problem5():    
    """
    2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
    What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
    
    Answer: 	232792560
    """
    from prime import primesbelow
    print("problem5:", production(primesbelow(20))*(2**3)*3)
    
def problem6():
    """
    The sum of the squares of the first ten natural numbers is,
    1**2 + 2**2 + ... + 10**2 = 385
    The square of the sum of the first ten natural numbers is,
    (1 + 2 + ... + 10)**2 = 55**2 = 3025
    Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 - 385 = 2640.
    Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
    
    Answer: 25164150
    """

def problem7():
    """
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
    What is the 10 001st prime number?
    
    Answer:   104743
    """
    from prime import primesbelow
    print("problem7:", primesbelow(10**6)[10000])
    
def problem10():
    """
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.    
    Answer:   142913828922
    """
    from prime import isprime
    print("problem10:", sum([i for i in range(2,2000000) if isprime(i)]))
    
def problem():
    problem1()
    problem3()
    problem5()
    problem6()
    problem7()
    problem10()
    
if __name__ == "__main__":
    timeit(problem)