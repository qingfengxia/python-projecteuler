# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
import math # math.sqrt()
# problems 9 :   factorial  primes
    
def Pythagorean_triplet_sum(sum):
    """Project euler P9:   Done!
    # Find the only Pythagorean triplet, {a, b, c}, for which a + b + c = 1000. 
    # Pythagorean triplet: a^2 + b^2 = c^2
    # c is the largest:   1000/(1+sqrt(2.0))<c<1000/2
    # a is the smallest:  
    """
    found = False
    for c in range(int(sum/2)-1 , int(sum/(1+2.0**0.5)) , -1):
        for b in range( c-1, int( c/ (2.0**0.5) ), -1):   # there may be bigger stride, 
            a = sum - b - c
            if( c*c - (a*a + b*b) != 0 ): 
                continue
            else:
                found = True
                print(a, b, c)  # 
                #if this tuple is unique! or plus to a list of tuple
                print("the product of a b c is : " , a*b*c)
                return (a, b, c)
    if(found  == False):
        print(("there is not Pythagorean triplet whose sum is ", sum))



############################## factor ##################################
"""
>>> def factorial(n):
c = factorial.dict.get(n)
if c:
return c
c = factorial(n-1)*n
factorial.dict[n] = c
return c
"""

def tuple_list_to_int_list(tl):
    s=[]  #list,  how to declear an empty set?
    for j in tl: 
        # permutations : NO repeated
        number=''
        for c in j :
            number=number+c
        s.append(int(number))
    return s

def factorial(N):
    """  N must be a int bigger than 1, recursively
         using the unlimited digits number of int of Python
    """
    result = 1L
    if N==2 :
        return  2
    else:
        result = factorial(N-1)* N
        return result

def digits(N,*arg):
    """  overload function, if there is no secondary parameters,
         all digits list generated for the lowest power
         default parameter seems better, can that contains expression?    
    """
    count = int( math.ceil(math.log10(N)) ) # ceil return float
    base = 10
    if(len(arg) >= 2):
        base=arg[1]
    if(len(arg) >= 1):
        count=arg[0]
    #
    t =N
    for i in range(count):
        d = t % base
        t = t/base
        yield d

def digits_list(N):
    """  Better way for base =10:
        sum([int(c) for c in str(N)])   
    """
    return [int(c) for c in str(N)]

def sum_Xdigits_factorN(N):
    """  
    """
    #type check will limit the usage of the function 
    #if type(N)!= type(1) and type(X)!= type(1):
    #    raise TypeError
    #if N<1 and X<1:
    #    raise ValueError
    #
     
    fac = factorial(N)
    X = int(math.ceil(math.log10(fac)))
#    s=fac%(10**X)
#    print s
#    dd=digits(s,X)
    dd = digits(fac)
    print(dd)
    print("sum of last ", X, "digits is :", sum(dd))


def sum_primes_below_N(N):
    """ Project euler P    Done !
    Find the sum of all the primes below two million, using the prime module
    """
    import prime  # import from current dir?
    s = 0
    s = sum(prime.primesbelow(N))
    print("sum of all primes below", N, "is : ", s)

def main():
    #import cProfile  # python -m cProfile myscript.py
    #cProfile.run("run()") # no input param supported, very detailed report, all func calls
    #timeit(Pythagorean_triplet_sum,1000)
    #timeit(sum_primes_below_N,2000000)
    # Find the sum of digits in 100!
    #sum_Xdigits_factorN(100)
    #print_spiral(9)
    #sum_diagnonals_spiral(1001)
    from timeit import timeit
    timeit(sum_primes_below_N,1000000)
    
if __name__ == "__main__":
    main()
