# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
problem 19 description:

You are given the following information, but you may prefer to do some research for yourself.

    1 Jan 1900 was a Monday.
    Thirty days has September,
    April, June and November.
    All the rest have thirty-one,
    Saving February alone,
    Which has twenty-eight, rain or shine.
    And on leap years, twenty-nine.
    A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.

How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?

weblink:

"""

from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#
from datetime import date, timedelta
import calendar

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

#leap is hard to understand:  1900 is not leap
def isleap(y):
    """ A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
    what is the range of year input,  calendar got isleap() function already!
    """
    if y%4==0 and ( not y%100==0):
        return true
    elif y%400==0:
        return true
    else:
        return false

def test():
    s=date(1900,1,1)
    print('weekday of start date: ',s.weekday())
    assert "s.weekday()==0"

def addmonths(sourcedate, months=1):
    month = sourcedate.month - 1 + months
    year = sourcedate.year + month // 12
    month = month % 12 + 1
    day = min(sourcedate.day,calendar.monthrange(year,month)[1])
    return date(year,month,day)

def bruteforce():
    #
    c=0
    s=date(1901,1,1)
    print('weekday of start date: ',s.weekday())
    while s.year<2001:
        if s.weekday()==6: c+=1          #monday ==0, so sunday ==6
        s=addmonths(s)
    print('Sundays fell on the first of the month during the twentieth century: ',c)

def problem():
    #test()
    bruteforce()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)