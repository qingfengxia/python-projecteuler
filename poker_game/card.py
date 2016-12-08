#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
card.py  
general definiation of single card of poker  ; 
from google-code project: python-poker 
"""


#面值序列
FACE=[ACE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE, TEN, JACK, QUEEN, KING]=range(13)
#花色序列：方块，梅花，红心，黑桃，鬼牌
SUIT=[DIAMOND, CLUB, HEART, SPADE, JOKER]=range(5)
#特殊牌：小鬼（王），大鬼（王）
SPECIAL=[BJOKER, RJOKER]=[52, 53]

#显示序列：
SFACE=['A', '2', '3', '4', '5', '6', '7', '8', '9','10', 'J', 'Q', 'K']
SSUIT=['Diamond', 'Club', 'Heart', 'Spade']
SJOKER=['Black-Joker','Red-Joker']


class Card(object):
    '''扑克牌类，描述某张扑克牌信息'''

    def __init__(self, *args):
        #牌编号
        self.id=None
        #花色
        self.suit=None
        #面值
        self.face=None
        #是否特殊牌
        self.special=False
        
        if len(args)==1:
            self.id=args[0]
            if self.id<52:
                self.suit=self.id/13
                self.face=self.id%13
            else:
               self.special=True
               self.suit=JOKER
               self.face=self.id
        elif len(args)==2:
            self.suit, self.face=args
            if self.suit==JOKER:
                self.id=self.face
                self.special=True
            else:
                self.id=self.suit*13+self.face
           
    def getSuit(self):
        if self.special:
            return None
        else:
            return self.suit
            
    def getFace(self):
        if self.special:
            return None
        else:
            return self.face
    
    def __str__(self):
        if self.special:
            return SJOKER[self.id-52]
        return '%s-%s'%(SSUIT[self.suit], SFACE[self.face])

if __name__ == '__main__':
    print Card(0), Card(1), Card(52), Card(CLUB, KING), Card(SPADE, ACE)
    card=Card(HEART, KING)
    r=[]
    a=Card(card.suit, (card.face+1)%13)
    b=Card((card.suit+1)%4, card.face)
    print a, b
