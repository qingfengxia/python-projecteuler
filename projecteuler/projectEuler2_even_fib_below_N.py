# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division

def sum_fibonacci_even_below_N(N):
        """  
        Solu1: generate the series and sum up, it seem very slow
        """
        fabm1= 2                #f1b(N-1)
        fabm2= 1                #fib(N-2)
        fab = fabm1+fabm2  # fib(3rd)
        nth = 3
        s=2   # only fab(2) is even
        if(N<3):
                print("the N is too small to calc fab series, N should > 3")
        while fab<N:  
                fabm2 = fabm1
                fabm1=fab
                fab = fabm1+fabm2
                nth = nth +1
                if (fab % 2) == 0:
                        s = s+fab
                        print(nth, fab)
                if (fab>N): break
        print("  The sum of the even-valued terms, which do not exceed four million, is:", s)	
        print("  the order of the biggest fab number bellow ", N, "is:", nth,"th")
        

sum_fibobacci_even_below_N(4000000) 