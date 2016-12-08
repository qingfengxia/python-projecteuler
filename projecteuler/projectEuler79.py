# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
A common security method used for online banking is to ask the user for three random characters from a passcode. For example, if the passcode was 531278, they may ask for the 2nd, 3rd, and 5th characters; the expected reply would be: 317.

The text file, keylog.txt, contains fifty successful login attempts.

Given that the three characters are always asked for in order, analyse the file so as to determine the shortest possible secret passcode of unknown length.
"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#
import itertools

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

filename="ProjectEuler79login.txt"
nlines=50  #
ndigits=3  # ask for three digit in ordered way


def test():
    # assert
    list=readlogin()
    digitsset=set("".join(list))
    print(digitsset)
    digitslist=[ d for d in digitsset]
    print(digitslist)
    #check if there is repeating char in single login3char
    rds=set()  # single repeating  not triple repeating 
    for v in list:
        if v[0]==v[1] or v[0]==v[2]:
            rds=rds+v[0]
        if v[1]==v[2]:
            rds=rds+v[1]
    print(rds)
    #
    for s in itertools.permutations("1123"):
        print(s)
    
def readlogin():
    #  projecteulerhelper.parseinputfile() is prefered 
    f=open(filename)
    lc=0
    ec=0
    list=[]
    for l in f.readlines():
        v=l.strip()  # line end is included in l
        if len(v) == ndigits:
            lc=lc+1
            list.append(v)
    if lc != nlines:
        print("error in reading all login data line")
        return None
    else:
        return list
        
def seqfit(seq, pw):
    pos=0
    for c in seq:
        pos=pw.find(c,pos)
        if  pos==-1:
            return False
    return True

def fitallseq(digitslist,  list):
    """if there is repeating digits,  itertools.permutations() is still usable
    if fail, still print some print, if i >= threshold, served as start point for new searching """
    for p in itertools.permutations(digitslist):
        #print "".join(pw)
        i=0
        pw="".join(p)
        for seq in list:
            if seqfit(seq,pw):
                i=i+1
                continue
            else:
                break
        if i==nlines:
            print("password sequence is found as:", pw)
            return True
    print("password is not found in all %d digits permutations", len(digitslist))
    return False
        
def bruteforce():
    """ brutal force seems possible, there is identical login3char, since only 50 logins
    there is no repeating digits found, also it is assumed all digits is used once!
    if these assumptions failed, try smarter method!
    it is found as: 73162890
    """
    list=readlogin()
    digitsset=set("".join(list))
    print(digitsset)
    npassword=len(digitsset)  # search start from non-repeating characters
    #
    digitslist=[ d for d in digitsset]
    if fitallseq(digitslist, list):
        print("%d digits password is found enough to fit all login seq " % npassword)


def smarter():
    """ heuristic build the password sequence, 
    """
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)