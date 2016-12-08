# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
Find the greatest product of five consecutive digits in the 1000-digit number.
"""
def text_to_int_list():
    # problem 8
    # max of consecutive 5 digis product,  
    #using multiple string of python,  error, 
    # or read file
    series=''
    fd=open(r'projectEuler8_digits1000.txt','r')
    # error can not find file???  there are an extra .txt after txt 
    i=0
    for l in fd.readlines():
        #series = series + str(int(l)) # need strip the "\n", but the last line is EOF no "\n"
        series = series + l[:50]   #  [start, stop_but_never_reach, step] just like range()
        i=i+1
        print("read line #", i, "length of line", len(l))  # last line has no \n
        #print "last char of line",l[-1] # newline except last line EOF 
        print(l)  # line 17 19 missing 1, because the leading zero is missing out
    #print series
    print("the length of the digits: ", len(series)) #998 ?
    if len(series) != 1000:
        print("incorrect digits length")
    #
    p=1
    index = 0
    for i in range(len(series)-5):
        tmp=int(series[i+4])*int(series[i+3])*int(series[i+2])*int(series[i+1])*int(series[i+0])
        if(tmp > p): 
                p=tmp
                index=i
    i=index
    print("max of consecutive 5 digis product:", p,"\nindex:", i+1, "\ndigits:",series[i:i+5])
    #40824
    
if __name__ == "__main__":
    text_to_int_list()