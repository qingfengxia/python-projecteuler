# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division

below10=['','one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine' ]
ten2nineteen=['ten',  'eleven', 'twelve', 'thirteen', 'fourteen', 'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']
tens=['', '','twenty', 'thirty', 'forty', 'fifty', 'sixty', 'seventy', 'eighty', 'nighty']

#from 1 to 100 

def countletteroflist(l):
    c=0
    for i in l:
        c+=len(i)
    return c
    
def lettercountfornumberbelow100():
    c=countletteroflist(below10)
    N=c
    N+=countletteroflist(ten2nineteen)
    for i in range(2,10):  #2-9
        N+=len(tens[i])*10+c
    return N

def lettercountfornumberbelow1000():
    # 
    c=lettercountfornumberbelow100()
    N=c
    for i in range(1,10):
        N+=len(below10[i])*100+len('handred')*100+len('and')*99+c      #100-199
    return N

def test():
    assert countletteroflist(below10)  == 36
    assert lettercountfornumberbelow100()  == 854

# correct at the first time trial!
N=lettercountfornumberbelow1000()
N+=len('one')+len('thousand')

test()
print(N)  #21124