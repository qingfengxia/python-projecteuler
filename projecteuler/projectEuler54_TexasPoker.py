# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem description:

In the card game poker, a hand consists of five cards and are ranked, 
from lowest to highest, in the following way:

High Card: Highest value card.
One Pair: Two cards of the same value.
Two Pairs: Two different pairs.
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.

The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for
example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example,
both players have a pair of queens, then highest cards in each hand are compared (see example 4
below); if the highest cards tie then the next highest cards are compared, and so on.

weblink:

Extension: from the third, or fourth card, test the probability to win

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 


import os, sys
sys.path.append(os.path.join(os.path.dirname(__file__), "../poker_game"))
from TexasHoldemPoker import *


def test():
    #
    # first line: "8C TS KC 9H 4S           7D 2S 5D 3S AC" 
    h1=[(CLUB,EIGHT),(SPADE,TEN),(CLUB,KING),(HEART,NINE),(SPADE,FOUR)]
    h2=[(DIAMOND,SEVEN),(SPADE,TWO),(DIAMOND,FIVE),(SPADE,THREE),(CLUB,ACE)]
    print(rank(h1))  #zero rank!
    print(rank(h2))
    print(cmphand(h1,h2))
    print('end of test()')
    
def bruteforce():
    #
    lh=[]
    f=open('ProjectEuler54poker.txt')
    for l in f.readlines(): # space seperated value
        lc=l.strip().split(' ')     #readline () strip the EOL  '\n'
        #print l,len(lc), lc
        list=[]
        for s in lc:
            # translate the double chars to card tuple        8C -> (DIAMOND, EIGHT)
            #s=s.strip().upper()  #
            list.append(translatecard(s))
        h1=list[:5]
        h2=list[5:]
        #print(rank(h1), rank(h2), cmphand(h1,h2))  #IO is more time consuming
        lh.append(cmphand(h1,h2))
    print('the first persion win over the second by hands number: ')
    print('total hands in this file/session', len(lh))
    #print lh  #359, if the pair are not sorted 
    print(sum([1 for w in lh  if w>0]))  #376
        
def smarter():
    pass
    
def problem():
    test()
    bruteforce()
    #smarter()

if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)