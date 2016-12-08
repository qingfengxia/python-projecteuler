# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 59
weblink:
description:

Each character on a computer is assigned a unique code and the preferred standard is ASCII (American Standard Code for Information Interchange). For example, uppercase A = 65, asterisk (*) = 42, and lowercase k = 107.

A modern encryption method is to take a text file, convert the bytes to ASCII, then XOR each byte with a given value, taken from a secret key. The advantage with the XOR function is that using the same encryption key on the cipher text, restores the plain text; for example, 65 XOR 42 = 107, then 107 XOR 42 = 65.

For unbreakable encryption, the key is the same length as the plain text message, and the key is made up of random bytes. The user would keep the encrypted message and the encryption key in different locations, and without both "halves", it is impossible to decrypt the message.

Unfortunately, this method is impractical for most users, so the modified method is to use a password as a key. If the password is shorter than the message, which is likely, the key is repeated cyclically throughout the message. The balance for this method is using a sufficiently long password key for security, but short enough to be memorable.

Your task has been made easy, as the encryption key consists of three lower case characters. Using cipher1.txt (right click and 'Save Link/Target As...'), a file containing the encrypted ASCII codes, and the knowledge that the plain text must contain common English words, decrypt the message and find the sum of the ASCII values in the original text.



Analysis:  input: single line comma sep  integer list
(1)a English dictionary is needed?   
(2) letter frequency stat:   e is 13%, t is 9%, space char  ?%
(3)or assume: there should be no some speical char in msg

python XOR op:    a^b        array("b", list)
convert ascii/int to bytes: 
    Python 2.X  b=''.join(chr(i) for i in myintegers) ->   b=bytearray(list)
    Python 3.X   bytes(myintegers)
"""

from projecteulerhelper import *
#timeit is encluded into projecteulerhelper now
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

from itertools import permutations, product 
import array    #bytearray


def load_msg(filename):
    with open(filename) as f:
        ls=f.readline().split(',')  # endofline is strip auto?
    #return array.array('B',[int(s) for s in ls]) # unsigned char 'B'
    return bytearray([int(s) for s in ls])

filename="ProjectEuler59XORcipher.txt"
msg=load_msg(filename)
pwset=bytearray([i for i in range(ord('a'), ord('z')+1)])
Npw=3
Nchunk=len(msg)//Npw

def decipher_msg(msg, pw):
    # return list of integer for sum
    return [ int(ch^pw[i%Npw])  for i, ch in  enumerate(msg) ]
#most conversative  printable  (32,127)   (48,57)  are digits,  space (127) is common should not be excluded
#printablecharbound=(32,127)   # no valid char is left, it means there is 

###################filter############################
blacklistbounds=( (0,31),(48,57) )     # >127 should not appear
def inblacklist(b):
    for i in range(len(blacklistbounds)):  # not efficient this line
        if (b >=blacklistbounds[i][0]) and (b<=blacklistbounds[i][1]): 
            return False
    return True

printablecharbound=[65,127]   # as the 
def isprintable(b):
    return b>=printablecharbound[0] and b<=printablecharbound[1] 
    
def validate_char(chunk,c):
    return all([isprintable(ch^c) for ch in chunk])
        
def blacklistfilter():
    pwchars=[]
    for ip in range(Npw):
        chunk=msg[ip:Nchunk*Npw:Npw]
        pwchars.append([ c for c in pwset  if validate_char(chunk,c) ])
        print("%dth password can only be :"%(ip+1), [chr(i) for i in pwchars[ip]])
        if len(pwchars[ip])==0:
            print("no char is left after this filtering, exit and retry")
            exit()
    return pwchars
    
##################stat########################
CHARSET_STAT={ord(' '): 0.13,
                            ord('e'): 0.13,
                            ord('t'): 0.09
                            }
def textstat(text, fp):
    """ @text: decipher msg, return a dict of stat 
    @stat:   dict with exact size of fingerprint dict: fp,  value is integer frequency
    """
    stat=fp  # copy keys from fingerprint dict
    #print stat
    for k in fp:   # for k,v in stat.iteritems()
        stat[k]=sum([k==c for c in text])
    return stat
    
def test_fingerprint(text, fp):
    """ @CHARSET_STAT: the fingerprint of langage,
        
    """
    l=float(len(text))
    threshold =1.0
    stat=textstat(text, fp)
    return all([ v>fp[k]/l *threshold   for k,v in stat.iteritems()])
        
##################dict########################        
def contain_words(text):
    # english dict may needed to reduce the password range
    return False

def dictlookup():
    pass
    
 
###########################################
    
def test():
    # assert
    print(pwset)
    print(range(0,Nchunk*Npw,Npw))
    print(msg[:16])
    print(msg[0:Nchunk*Npw:Npw])   # does not support range as indice?
    assert msg[-1]==73

def bruteforce():
    """ permutations() means the password contains non-repeated char
    to save time, test only first servarla bytes of the message, 
    to reduce the search range, test each char in charset, 
    """
    pwlist=[]
    for p in product(pwset, repeat=Npw):
        #print p   #tuple,  can not convert to bytearray(tuple)
        pw=bytearray([i for i in p])
        text=decipher_msg(msg,pw)
        if test_fingerprint(text, CHARSET_STAT):
            pwlist.append(pw)
          
    if len(pwlist) !=1:
        print("too many passwords found, try to reduce!", len(pwlist))
    else:
        key=pwlist[0]
        print("password found as:", key)
        text=decipher(msg, key)
        print("sum of the ASCII values in the original text:", sum(text))

def smarter():
    pass
    
def solve():
    bruteforce()
    #smarter()
    
if __name__ == "__main__":
    #test()
    timeit(solve)
    #timeit(func, param)