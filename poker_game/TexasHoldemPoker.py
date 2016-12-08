#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
This file is special for Texas Holdem Poker
##############################################
card.py  general definiation of poker ; from python-poker google-code project
simplified class into tuple (suit, face)/named tuple:  hand=[card0 card1 ...] 
e.g. Card(CLUB, THREE)      #    id=0-53     

#  BE CAREFUL !!!              TEN == 9, KING=12, since ACE==0
# Using the face constants instead of int number!!!

# Poker Glossary: http://www.pokertips.org/glossary/glossary.php

##############################################
Is ace 2 3 4 5 a straight?

Depends on the game and/or how the dealer has called it. 
If by rule or by call it's "aces high," then no.

In EulerProject P54 it is ACEHIGH rule

###############################################
#calc probability of each rank, it can be found on internet
#see blog: "Classifying and Ranking Poker Hands in Python"
# From 1000000 hands: monte carlo method, not theory!
# it applys to empty hand, no card is hand out to playeres

    High Card: A hand with no other classifications. (50%)
    One Pair: A hand with a single pair of same rank cards. (42%)
    Two Pair: A hand with two pairs of same rank cards. (4.75%)
    Three of a Kind: A hand with three cards of the same rank. (2.1%)
    Straight: A hand with cards whose ranks are numerically in sequence. (0.39%)
    Flush: A hand with cards whose suits are all the same. (0.2%)
    Full House: A hand with both Two Pair and Three of a Kind. (0.14%)
    Four of a Kind: A hand with four cards of the same rank. (0.024%)
    Straight Flush: A hand that is both a straight and a flush. (0.0015%)

def win(my, others):     #calc odds to win if I have four cards 

################rank###################
#sorting before ranking 
#sorted first by decreasing, also by suit 
#decision tree:  
High Card[0] 
            -> flush ->straight flush ->Royal
               else: -> straight 
                     ->has pair :according to len(set(faces))
                      Make sure, the call resortpair(h) before compare
                        TotalCards -1  ->    one pair
                        TotalCards-2   ->    -> Two pairs
                                             -> three of a Kind     
                        TotalCards = 3  ->   -> full house
                                             -> four of a Kind                          
                
"""



# sort it deal with JQKA,  
# check it the rank 
#marked hand of cards by (rank, GreatestCard)

#pool of total/remined cards as a set():  cardbox

###################class hand.py############################
from __future__ import print_function
from card import *    # defination of constants  card FACE and suit

ACEHIGH = 13
ACELOW = 0
DefinedAceHighRule=True
DefinedAceBothHighAndLow = False  #usful in straight judge
if DefinedAceHighRule:
    ACE=ACEHIGH      #replace the defination in card.py !
else:
    ACE=ACELOW
    
TotalCards=5  # the total cards, usually 5, but this program should apply to 3 
iFace=1  #index of Face in card tuple
iSuit=0  # extend the card class, to make it indxable or  derived from userdict


RANK=[HIGHCARD, ONEPAIR, TWOPAIRS, THREEOFAKIND, STRAIGHT,
            FLUSH,  FULLHOUSE, FOUROFAKIND, STRAIGHTFLUSH, ROYALFLUSH]=range(10)
#printable string name of rank            
SRANK=['High Card', 'One Pair', 'Two Pairs', 'Three of a Kind' , 'Straight' ,
            'Flush',  'Full House', 'Four of a Kind', 'Straight Flush', 'Royal Flush']
            
#class Hand(object):
    #def __init__(args):
        
class CardError(Exception):
    def __init__(self, msg):
        self.value=msg
    
def sort(h): 
    """  ACE is treated as ACEHIGH or ACELOW, depends on settings
    """
    return sorted( h, key=lambda card: card[iFace])   #Fail here!
    
def isflush(sh):
    """ applied to TotalCards>=3
    """
    sl = [c[iSuit] for c in sh]
    #if [c.getsuit() for c in sh]:               # if  using class Card
    if sl.count(sl[0]) == TotalCards:
        return True
    else:
        return False
        
def isstraight(sh):
    """ 10 J Q K A  should be considered as straight in isstraight() 
    ACE ('A')  is the int ACEHIGH or ACELOW,  if DefinedAceHighRule == True
    applied to TotalCards>=3
    """
    #print sh[0][iFace], SFACE[sh[0][iFace]]
    fl=[c[iFace] for c in sh]
    # fl=[c[iFace] for c in sh]        # if using class Card
    if len(set(fl)) == TotalCards :
        # [ACE, TEN, JACK,QUEEN,KING]     [ACE, QUEEN,KING]
        if fl[-1]-fl[0]==TotalCards-1 :
            return True
        elif DefinedAceBothHighAndLow:
            if DefinedAceHighRule \
                  and (fl[0] == TWO and fl[-1]==ACE and fl[-2]-fl[0]==TotalCards-2):
                print('found [ACE,  TWO  THREE ,FOUR, FIVE]  as straight')
                return True
            # [ACE, TEN, JACK,QUEEN,KING]     [ACE, QUEEN,KING]
            elif (not DefinedAceHighRule) \
                   and (fl[0] == ACE and fl[-1]==KING and fl[-1]-fl[1]==TotalCards-2):
                print('found [ACE, TEN, JACK,QUEEN,KING]  as straight, and ACE=',ACE)
                return True
            else: return False
        else:
            return False
    else:
        return False

def rankpair(sh):
    """ as it is not straight or flush, it must contains pair or no pair(HIGHCARD)
    TWOPAIRS FULLHOUSE, FOUROFAKIND  only applied to TotalCards=5 or 3 
    """
    lf=[c[iFace] for c in sh]
    sf=set(lf)
    l = len(sf)
    if l== TotalCards :
        return HIGHCARD
    elif l==TotalCards-1 :
        return ONEPAIR
    elif l==TotalCards-2 :
        if  max([lf.count(f) for f in sf]) == 3 :
            return THREEOFAKIND
        elif TotalCards==5 and max([lf.count(f) for f in sf]) == 2 :
            return TWOPAIRS
        else:
            raise CardError('Total card number {0} is not implemented in Texas holdem'.format(TotalCards) )
    # only applied to TotalCards=5, # for the other ranks: TWOPAIRS FULLHOUSE, FOUROFAKIND
    elif l==TotalCards-3:
        if  TotalCards==5 : 
            minfacecount=min([lf.count(f) for f in sf])  # acount of same face
            if minfacecount==2:
                return FULLHOUSE
            if minfacecount==1:
                return FOUROFAKIND
        else:
            raise CardError('Total card number {0} is not implemented in Texas holdem'.format(TotalCards) )
    else:
        raise CardError('Logical error when rankpair() with total cards = {0}'.format(TotalCards)  )
    
def rank(h):
    """ there is no card face check,  it is dealer ' duty to exclude JOKERs
    """
    sh=sort(h)  
    r=HIGHCARD  # High Card, the most common hand, smallest in rank
    #decision tree
    if isflush(sh):
        r=FLUSH
        if isstraight(sh):
            r=STRAIGHTFLUSH
            if sh[0][iFace] ==TEN:    # 10 J Q K A  should be considered as straight in isstraight()
                r=ROYALFLUSH
    else:
        if isstraight(sh):
            r=STRAIGHT
        else:
            r=rankpair(sh)
    #print r, sh
    return r,sh
    
def resortpair(h):
    lf=[c[iFace] for c in h]
    sf=set(lf)
    # key=lambda k:k[1] is not needed, it should work for tuples, if count is equal, compared the second element of tuples!
    fc=sorted([(lf.count(f), f) for f in sf])  #reverse=True
    #TWOPAIRS is tricky to deal with
    sh=[]
    for f in fc:
        sh+=[c for c in h if c[iFace]==f[1]]  #find item in h, then append, 
    return sh
    
#~ def resortpair(rk, h):
    #~ #resort is needed during rankpair, then the pair can be compared!!!
    #~ if rk==ONEPAIR:
        #~ #
    #~ elif rk==TWOPAIRS:
        #~ #
    #~ elif rk==THREEOFAKIND:
        #~ #
    #~ elif rk==FULLHOUSE:
        #~ #
    #~ else: #FOUROFAKIND
        #~ #
        
def resortace(h): 
    """swap/spin ACEHIGH and ACELOW and resort it,
    it is tricky to deal with straight, 
    """
    if DefinedAceHighRule:
        ACESPIN=ACELOW
    else:
        ACESPIN=ACEHIGH
    sh=h
    for i,c in enumerate(h): 
        if c[iFace]== ACE:
            sh[i]=(c[iSuit], ACESPIN)
        #do nothing, return it back, no memory copy 
    sh=sort(sh)
    return sh
    
def cmphighcard(sh1,sh2):
    for i in range(len(sh1)-1,0,-1):
        fdiff = sh1[i][iFace] - sh2[i][iFace] 
        if fdiff != 0:
            break  #break out of this loop
    return fdiff/10.0  #make it 
    
def cmphand(h1,h2):        # name comflict with std func __cmp__ ??
    """compare rank first, then compare the face of card sequence
    card suit is not compared!
    ACE is treated as biggest, need to be compared if rank is identical

    test  the len of h1 and h2 is not done
    """
    (r1,sh1)=rank(h1)
    (r2,sh2)=rank(h2)
    if r1==r2: # identical RANK,  resort as pair, then compare the high card
        sh1,sh2=resortpair(sh1), resortpair(sh2)
        ret=cmphighcard(sh1,sh2)
        if DefinedAceBothHighAndLow and r1==STRAIGHT and sh1[-2][iFace] == SIX :   
            sh1=resortace(sh1)
            sh2=resortace(sh2)
            ret=cmphighcard(sh1,sh2)
        return ret
    else:
        return float(r1-r2)

def win(my, others):
    """
    my: one hand with 2/4 cards, waiting for last cards
    others:  list of hands for other, each with same len of cards as me
    
    calc my odds to win the other before last card is sent to you,
    # random select nTotalPlayers cards from the remind cards box: 52-8 cards
    and get each players final rank for each card -> building a list/odds matrix
    do NOT distinguish the forehand, assume each one got the final card at same time
    """
    nCompleteCards = 52
    nReceivedCards = len(my)
    nTotalPlayers = len(others)+1
    if nTotalPlayers <2:
        print("Error: no enough players for game: %d " % nTotalPlayers)
    nRemainedInCardBox = nCompleteCards - nTotalPlayers * nReceivedCards
    if nRemainedInCardBox < nTotalPlayers:
        print("Error: no enough cards for total palyers %d " % nTotalPlayers)
    #get the complete cards (52) , exclude the handed out cards  , build the cardBox as a set 
    import itertools 
    # get last card for nTotalPlayers, combinations 
    # permutation for each players. 
    #calc rank 
    #built the odds matrix 
    #statistics
    

def translatecard(s):
    """  stranslate from string  '9H' -> (HEART, NINE)  T->10, 
    served as adapter for card.py, 
    assume it is upper case and len=2 or 3 ( only for card face TEN e.g.'10H' 'TH' )
    JOKER is test firstly,  
    """
    if  s=='NB' or s=='NTB' or s=='NTL':         # this is format dependent!, 
        suit=JOKER
        face=BJOKER
    elif s=='NR' or s=='NTR' or s=='NTG':
        suit=JOKER
        face=RJOKER
    else: #parse face           or using str.replace()
        if s[0] == 'T':  #
            face=TEN
        elif s[0] == 'J':  #
            face=JACK
        elif s[0] == 'Q':
            face=QUEEN
        elif s[0] == 'K':
            face=KING
        elif s[0] == 'A':
            face=ACE
        elif s[0].isdigit():
            face=int(s[:-1])-(2-TWO) #  (2-TWO) may be 0 or 1
            #except ValueError as e:
            #    print e.msg()
            #there mey be exception, catch   the typecast error!
        else:
            raise CardError("Unexpected char during parse the card face from str: {0}".format(s))
        # parse suit
        if s[-1] == 'D':
            suit=DIAMOND
        elif s[-1] == 'C':
            suit=CLUB
        elif s[-1] == 'H':
            suit=HEART
        elif s[-1] == 'S':
            suit=SPADE
        else:
            raise CardError(" Fail to decode suit info from str: {0}".format(s))   
    return suit,face
    
######################################################
def test():
    #
    print("all the output should be pair of False and True ")
    #
    print(translatecard('10S')) # (3, 10)
    print(translatecard('9D'))
    #
    assert("rankpair([(1,3), (1,3), (1,3), (1,5), (1,5)])==FULLHOUSE")
    assert("rankpair([(0,3), (1,3), (1,3), (1,5), (1,5)])==TWOPAIRS")
    #
    unsortedhand=[[0,ACE], [0,TEN], [1,JACK], [1,QUEEN], [1,KING]]
    print('test sort()',sort(unsortedhand))   #Fail, why?  face and suit is in wrong place
    print('Should be straight: ',SRANK[rank(unsortedhand)[0]])
    
    if DefinedAceBothHighAndLow:
        print(resortace(unsortedhand))
        print('ACE=', ACE)
        small_straight=[[1,TWO], [1,THREE], [1,FOUR], [1, FIVE], [0,ACE]]
        print('DefinedAceBothHighAndLow, then', small_straight)
        print('Should be straight: ',SRANK[rank(small_straight)[0]])
    # 
    print(isflush([(0,0), (1,3), (1,4), (1,5), (1,6)]))
    hand_flush=[(1,0), (1,3), (1,4), (1,5), (1,6)]
    print(isflush(hand_flush))
    print('Should be flush: ',SRANK[rank(hand_flush)[0]])  #error here!
    #
    print(isstraight([(1,0), (1,3), (1,4), (1,5), (1,6)])) # should be False
    hand_straight=[(0,2), (1,3), (1,4), (1,5), (1,6)]
    print(isstraight(hand_straight))
    #
    h=[(1,0), (1,5), (1,5), (1,2), (1,2)]
    print('resort two pairs',resortpair(h))
    #
    print(cmphand(hand_straight,hand_flush))
    print(cmphand(hand_straight,hand_straight))

    print('end of test()' )
    
if __name__ == "__main__":
    test()