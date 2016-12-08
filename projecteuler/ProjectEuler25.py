# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division

"""Problem 25
The Fibonacci sequence is defined by the recurrence relation:
    Fn = Fn-1 + Fn-2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

    F1 = 1
    F2 = 1
    F3 = 2
    F4 = 3
    F5 = 5
    F6 = 8
    F7 = 13
    F8 = 21
    F9 = 34
    F10 = 55
    F11 = 89
    F12 = 144

The 12th term, F12, is the first term to contain three digits.

What is the first term in the Fibonacci sequence to contain 1000 digits?

##################################################
"""
from fibonacci import *
from math import log

def problem25(Ndigits):
    assert "Ndigits==1000"
    base=100 # search by base+i*step  2*base  3*base ...
    #the base can be estimated by  
    print("the n is apporximately =",log(10,fib_ratio)*(Ndigits-9)+40)  #40th is first 9 number
    # for each 100fib, the digits + 21
    step=100 #
    loopMax=20000  #step max
    nth=-1  # indicate error or uncalculated
    t_step=(fib(step), fib(step+1), step)
    t0=( fib(base), fib(base+1), base) # should be an input parameter
    l=[t0]
    t1= fib_K_plus_L(t0, t_step)
    l.append(t1)
    print(l)
    #
    start=2
    i=start-1
    digits=digits_count(l[i][0]) #
    while  digits < Ndigits:    
        #n=K+L
        t= fib_K_plus_L(l[i],t_step)
        l.append(t)  
        
        digits=digits_count(t[0]) # 
        #
        nth=t[2]
        i=i+1  
                
        print("search to nth={0}, digits={1}, list len={2} ".format(nth, digits, len(l)))   
           
        if i>loopMax:
            print("Loop:", loopMax, "is reached, without reaching a number with digits", Ndigits)
    
    ################roll back to i-2###################
    i_floor=len(l)-2
    (fn, fnp1, nth) = l[i_floor]
    #nth=base+(i_floor)*step
    digits=digits_count(fn)
    print("searching start at nth={0}, digits={1}".format(nth, digits))
    
    # simple test by +1 increasement!  test by ratio's expotential?
    while digits_count( fn ) < Ndigits:
        tmp=fnp1+fn  # there must be a tempary value to store the fnp2
        fn=fnp1
        fnp1=tmp
        nth=nth+1
    
    print("{} th fab number has {} digits".format(nth, digits_count( fn )))
    #print(nth-1, digits_count( fnp1-fn))
    
if __name__ == "__main__":
    problem25(1000)