from prime import *

# https://comeoncodeon.wordpress.com/2010/09/18/pollard-rho-brent-integer-factorization/
def pollard_brent(n):
    if n % 2 == 0: return 2
    if n % 3 == 0: return 3

    y, c, m = random.randint(1, n-1), random.randint(1, n-1), random.randint(1, n-1)
    g, r, q = 1, 1, 1
    while g == 1:
        x = y
        for i in range(r):
            y = (pow(y, 2, n) + c) % n

        k = 0
        while k < r and g==1:
            ys = y
            for i in range(min(m, r-k)):
                y = (pow(y, 2, n) + c) % n
                q = q * abs(x-y) % n
            g = gcd(q, n)
            k += m
        r *= 2
    if g == n:
        while True:
            ys = (pow(ys, 2, n) + c) % n
            g = gcd(abs(x - ys), n)
            if g > 1:
                break

    return g

smallprimes = primesbelow(1000) # might seem low, but 1000*1000 = 1000000, 
#so this will fully factor every composite < 1000000


def primefactorize(n, sorting=True):
    #using pollard_brent method
    factors = []

    limit = int(n ** .5) + 1
    for checker in smallprimes:
        if checker > limit: break
        while n % checker == 0:
            factors.append(checker)
            n //= checker
            limit = int(n ** .5) + 1
            if checker > limit: break

    if n < 2: return factors

    while n > 1:
        if isprime(n):
            factors.append(n)
            break
        factor = pollard_brent(n) # trial division did not fully factor, switch to pollard-brent
        factors.extend(primefactorize(factor)) # recurse to factor the not necessarily prime factor returned by pollard-brent
        n //= factor

    if sorting: factors=sorted(factors)

    return factors

def factorization(n):
    """
    """
    factors = {}
    for p1 in primefactorize(n):
        try:
            factors[p1] += 1
        except KeyError:
            factors[p1] = 1
    return factors

totients = {} 
def totient(n):
    if n == 0: return 1

    try: return totients[n]
    except KeyError: pass

    tot = 1
    for p, exp in factorization(n).items():
        tot *= (p - 1)  *  p ** (exp - 1)

    totients[n] = tot
    return tot
    
    
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

def gcd(a, b):
    if a == b: return a
    while b > 0: a, b = b, a % b
    return a

def lcm(a, b):
    return abs(a * b) // gcd(a, b)
