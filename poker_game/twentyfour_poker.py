""" 
Game twenty-four point: practice kids' mental arithmetic capability 

Rule: 

two/four players, who show two/onecards simultanously, 
try to make 3 arithmetic operations ( only four integer operaton+ - * / )
based on the four cards with number (1-10, J Q K are regarded as one)  only once to get 24 
who give the solution first, will win all four cards back. (no solution is also a result)
Finally, the player with most cards win!

Example:
4 7 A 5  ->   4*7-5+1=24

why 24 is chosen?   1*2*3*4=24,  24 has the most dividers!

this python script will try to search solution, 
but total cards counts and final result(24 in this game) is parameterized, 
it could extended to  5 cards to get 120, but f() need to be rewritten!

 currently tested only with python 2.x, uisng 2to3 should make it work with python 3.x
 
 Author: Qingfeng Xia
 Lisense : BSD 4 clause
 2012-12-10
"""

from __future__ import print_function    
from itertools import combinations, product,permutations

N=4   # count of cards
M=24
op=['+','-','*','/']  #since the calculation is done by float , no need to use //
d=[float(i) for i in range(1,10)]

def f(tp,top,M,expr=False):
    """this function will evaluate one digits and arithmetic organization,
    Valid only for N=4
    """
    #e1='(({0[0]}{1[0]}{0[1]}){1[1]}{0[2]}){1[2]}{0[3]}=={2}'.format(tp,top,M) #not necessary for permutation
    e2='({0[0]}{1[0]}({0[1]}{1[1]}{0[2]})){1[2]}{0[3]}=={2}'.format(tp,top,M)
    #print e2
    if expr:
        r=[]
        #if eval(e1): r.append(e1)
        if eval(e2): r.append(e2)
        return r
    else:
        #return eval(e1) or eval(e2)
        return  eval(e2)

def test_expr(td,M=24):
    """ print possible solution for  td: tuple of four card point
        int division is hard to test for a%b==0, so change to float division
    """
    l=[]
    dlist=[float(d) for d in td]
    for tp in permutations(dlist):  #each card is used once
         for top in product(op,repeat=N-1):   #using product 
             l+= f(tp,top,M,True)
    if len(l)==0:
        print(td,'this number tuple can not make',M)
        return []
    else:
        return l

def test():
    top=('-','-','*')
    tp=('3','4','5','6')
    print(test_expr(tp,24))
    print(f(tp,top,24))
    #print product(op,repeat=N-1)
    print('End of test')
    
def findnosolutiontuple():
    for td in combinations(d,N):
        l=[]
        for tp in permutations(td):
            l.append( any([f(tp,top,M) for top in product(op,repeat=N-1) ] ) )
        if not   any(l):
            print('this number tuple can not make 24',td)
 
if __name__ == "__main__" :
    test()
    findnosolutiontuple()
    