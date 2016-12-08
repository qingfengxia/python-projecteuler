# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
def money_changes():
    """  s: sum must be the multiple of token[i]
    this method is very slow >1 hour, a curseive method may be prefered 
    """
    # method 1, slow >0.1 hr
    #  got incorrect result: 73681+1
    # line continuation token? \  or implicit without any token like C++
    s=200
    token=[100,50,20,10,5,2,1,200]
    count=1  # the 200 coin is not count formerly
    count=count+1  # the 2X100 coins 
    for i0 in range( int(s/token[0]) ):
        for i1 in range(int(s/token[1])+1 ):
            for i2 in range( int(s/token[2])+1 ):
                for i3 in range(int(s/token[3])+1 ):
                    for i4 in range(int(s/token[4])+1 ):
                        for i5 in range(int(s/token[5])+1 ):
                            for i6 in range(int(s/token[6])+1 ):
                                if i0*token[0] + i1*token[1] + i2*token[2] + i3*token[3] + i4*token[4] + i5*token[5] + i6*token[6]== s:
                                    count = count +1
    return count
    
def recursively_find_changes(s, token):
    """  
    method 2 recursively find the method
    # result: 73682  
    """
    # line continuation token? \  or implicit without any token like C++
    #stop of the recursive method 
    if len(token) == 1:
        if s%token[0] == 0:   # s=0 ? return 1; 
            return 1          #token[-1] == 1, it must be true
        else:
            return 0
    else: # len>1
        count=0
        #if(s%token[0] == 0): count = count +1 # all using one kind of change, 
        #error: do NOT acount that s%token[0] != 0
        #count = count + recursively_find_changes(s, token[1:])# do not use this kind of change
        for i in range( 0, int(s/token[0])+1 ):   #     
            count = count +recursively_find_changes(s-i*token[0], token[1:]) # all using one kine change
        return count
    
           
def find_changes():
    token=[200,100,50,20,10,5,2,1]
    s=200
    #count = money_changes(s, token)
    count = recursively_find_changes(s, token)
    print("count of diff changes arrangement method for total",s,"is: ", count)  # count = 1783
    print("using the changes type", token)
 
def main():
    from timeit import timeit
    timeit(find_changes)

if __name__ == "__main__":
    main()
