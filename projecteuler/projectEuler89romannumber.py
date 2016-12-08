# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
The rules for writing Roman numerals allow for many ways of writing each number (see About Roman Numerals...). However, there is always a "best" way of writing a particular number.

For example, the following represent all of the legitimate ways of writing the number sixteen:

IIIIIIIIIIIIIIII
VIIIIIIIIIII
VVIIIIII
XIIIIII
VVVI
XVI

The last example being considered the most efficient, as it uses the least number of numerals.

The 11K text file, roman.txt (right click and 'Save Link/Target As...'), contains one thousand numbers written in valid, but not necessarily minimal, Roman numerals; that is, they are arranged in descending units and obey the subtractive pair rule (see About Roman Numerals... for the definitive rules for this problem).

Find the number of characters saved by writing each of these in their minimal form.

Note: You can assume that all the Roman numerals in the file contain no more than four consecutive identical units.

======================================================
How do you read and write Roman numerals?

Traditional Roman numerals are made up of the following denominations:

I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

You will read about many different rules concerning Roman numerals, but the truth is that the Romans only had one simple rule:

Numerals must be arranged in descending order of size.

For example, three ways that sixteen could be written are XVI, XIIIIII, VVVI; the first being the preferred form as it uses the least number of numerals.

The "descending size" rule was introduced to allow the use of subtractive combinations. For example, four can be written IV because it is one before five. As the rule requires that the numerals be arranged in order of size it should be clear to a reader that the presence of a smaller numeral out of place, so to speak, was unambiguously to be subtracted from the following numeral. For example, nineteen could be written XIX = X + IX (9). Note also how the rule requires X (ten) be placed before IX (nine), and IXX would not be an acceptable configuration.

Generally the Romans tried to use as few numerals as possible when displaying numbers. For this reason, XIX would be the preferred form of nineteen over other valid combinations, like XVIIII or XVIV. However, this was NOT a rule and there still remain in Rome many examples where economy of numerals has not been employed. For example, in the famous Colesseum the the numerals above the forty-ninth entrance is written XXXXVIIII and not IL nor XLIX (see rules below).

Despite this, over time we have continued to introduce new restrictive rules. By mediaeval times it had become standard practice to avoid more than three consecutive identical numerals. That is, IV would be written instead of IIII, IX would be used instead of VIIII, and so on. In addition, the subtractive combinations had the following rules superimposed:

    Only I, X, and C can be used as the leading numeral in part of a subtractive pair.
    I can only be placed before V and X.
    X can only be placed before L and C.
    C can only be placed before D and M.

These last four rules are considered to be law, and generally it is preferred, but not necessary, to display numbers using the minimum number of numerals. Which means that IL is considered an invalid way of writing forty-nine, and whereas XXXXVIIII, XXXXIX, XLVIIII, and XLIX are all quite legitimate, the latter is the preferred (minimal) form.

It is also expected that higher denominations should be used whenever possible; for example, L should be used in place of XXXXX, or C should be used in place of LL. However, even this "rule" has been flaunted: in the church of Sant'Agnese fuori le Mura (St Agnes' outside the walls), found in Rome, the date, MCCCCCCVI (1606), is written on the gilded and coffered wooden ceiling; I am sure that many would argue that it should have been written MDCVI.

However, if we believe the adage, "when in Rome do as the Romans do," and we see how the Romans write numerals, then it clearly gives us much more freedom than many would care to admit.
"""


from projecteulerhelper import *
#timeit is import from helper, instead of timeit module
#

# test the correction by a small dimension first. 
# test  brute force first, method1
#then, try some smart method! 

filename="ProjectEuler89romannumber.txt"
import roman
DEBUG=True


parsedict={'M':  1000,
                   'D': 500,
                   'C':  100,
                   'L':  50,
                   'X':  10,
                   'V':  5,
                   'I': 1}
LEVELS=sorted([v for k,v in parsedict.items()])
def parseroman(s):
    """ parse from end to begin, as descending rules is applied 
    error?
    """
    if not s:
        raise roman.InvalidRomanNumeralError, 'Input can not be blank or None'
    n=0 #result 
    i=len(s)-1  #string index
    l=0 #level index
    while i>=0:
        if parsedict[s[i]]==LEVELS[l]:
            n+=parsedict[s[i]]
        elif parsedict[s[i]]<LEVELS[l]:  # only one level less?
            if DEBUG :
                if parsedict[s[i]] < LEVELS[l-1] and  parsedict[s[i]]<LEVELS[l-2]:  #logic short circuit 
                    print("string: %s disobey the subtractive pair rule"%s)
            n=n-parsedict[s[i]]
        else:
            n+=parsedict[s[i]]
            while (parsedict[s[i]]!=LEVELS[l]):
                l+=1
        i-=1
    if n>0: 
        return n
    else:
        print("error in parse roman number: %s"%s)
            
# copy from roman module
romanNumeralMap = (('M',  1000),
                   ('CM', 900),
                   ('D',  500),
                   ('CD', 400),
                   ('C',  100),
                   ('XC', 90),
                   ('L',  50),
                   ('XL', 40),
                   ('X',  10),
                   ('IX', 9),
                   ('V',  5),
                   ('IV', 4),
                   ('I',  1))
                   
def toRoman(n):
    """convert integer to Roman numeral, the most optimistic represent
    the key to  generate the optimistic repr, is add 4 9 40 90 ..."""
    if not (0 < n < 5000):
        raise OutOfRangeError, "number out of range (must be 1..4999)"
    if int(n) != n:
        raise NotIntegerError, "decimals can not be converted"
    result = ""
    for numeral, integer in romanNumeralMap:
        while n >= integer:
            result += numeral
            n -= integer
    return result
    
def lineparse(l):
    i=parseroman(l.strip())
    #if i != count_roma(l.strip()):         print l.strip()
    return i

def smarter():
    """ python has a module, roman.toRoman() which gives the optimistic repr
    but fromRoman does not parse the non-optimistic string          
    """
    rnlist=parseinputfile(filename,lineparse)
    #originallen= 9106+743
    s=0
    with open(filename) as f:
        for l in f.readlines():
            s+=len(l.strip())
    rs=sum([len(roman.toRoman(rn)) for rn in rnlist])
    print("sum of char in orginal file is:",s)
    print("sum of roman number char  is: ", rs)
    print("char space reduced:", s-rs)

def test():
    #
    assert parseroman('VVIIIIII')==16
    assert parseroman('CMLXXXVII')==987
    assert toRoman(987)=='CMLXXXVII'
    assert parseroman('MMCCCLXIV')==2364
    assert parseroman('MMMMDCCCCXXXXVI')==4946
    print(toRoman(4946))
    
    
def method1():
    """ copy from internet, which is faster
    """
    f=open(filename)
    d=""
    g=""
    s=f.readline()
    while(s!=""):

     g=g+s
     s=s.replace("DCCCC", "CM")
     s=s.replace("LXXXX", "XC")
     s=s.replace("VIIII" , "IX")
     s=s.replace("IIII" , "IV")
     s=s.replace("XXXX", "XL")
     s=s.replace("CCCC" , "CD")
     d=d+s
     s=f.readline()
    print("result by string substition:",len(g)-len(d))
    print("most effective repr len:",len(d)) # does not strip the end of line, so it is higher than my calc

def problem():
    test()
    #method1()
    smarter()
    
if __name__ == "__main__":
    timeit(problem)
    #timeit(func, param)
