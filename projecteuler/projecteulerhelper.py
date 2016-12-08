
""" some utility func can be shared to solve
"""
from __future__ import print_function

def timeit(func, *param):
    """   Python has already get timeit module in std lib
         (1) Pass function as parameter
         (2) profiling
    In windows clock() counts in real time and at much higher resolution than time().
    Under windows time() counts in 1ms steps
    wheras it usually counts in 1us steps under linux.
    """
    import time
    #default for Windows
    tick_per_second=1  # how big is it for Windows
    #timer=time.clock     #func assignment?
    #test the platform 
    import platform
    if platform.system() == 'Windows':
        tick_per_second=1 # how big is it for 
        #timer=time.clock
    t0=time.clock()
    if len(param)==0:
        func()
    else:
        print("len of parameters for timeit module: ", len(param))
        func(*param)  #unpack the list/tuple
    t= ( time.clock() - t0 ) / tick_per_second
    print("The time spent on " , func.__name__, "is : ", t, " Second in Python")


####################### IO #########################
def parseinputfile(filename, lineparser, errordetector=None):
    """ parse input  text input file with multiple lines, return a list of object
    each line is parse by func: linepaser, return object ,in most case, a list of user defined element
    errordetector=None, means no line parser result check,  
    errordetector: take  line parser result list as the only input
    """
    f=open(filename)
    lc=0
    ec=0
    list=[]
    for l in f.readlines():
        li=lineparser(l)
        if (errordetector!= None) and  errordetector(li):
            #print li
            ec=ec+1  # error in parse line
        else:
            list.append(li)
            lc=lc+1
    #reporting 
    if ec>0:
        print("error happens in parse line")
        return None
    else:
        print("%d lines has been successfully parsed"%lc)
        return list

def ReadMat( fileName, sep):   
    """    parseinputfile is prefered since it is a more general solution"""
    file=open(fileName,'r')
    lines = file.readlines()
    i=0
    table=[]
    for l in lines:
        table.append( [int(num)  for num in l.split(sep)]  )
        i=i+1
    print(i, "lines have been read to list of list")
    return table

def ReadBigInt(fileName, nd):
    file=open(fileName,'r')
    i=0
    ll=[]
    lines = file.readlines()  # optional param: size is the total byte size: lines*len(len)
    for line in lines:
        #line = file.readline()
        #if not line: break
        ll.append( [int(line[nd*i:nd*(i+1)])  for i in range(int( len(line)/nd) )]  )
        i=i+1
    file.close()
    print(i," line has been read!")  #why only 10 lines?
    return ll
    
################################################
def circularNo(N):
    # yield is generator just like return a list 
    # 101  -> 011, how to deal circularNo with zero?
    # filtered out the number with same digits?  1311 1311
    #
    # how to set the type of parameter in python?  isinstance()  type()
    # reserve space for a list/array for better performance  -> yield
    # ndigits = int( math.ceil(math.log10(N))  )  # -> len(dc)
    dc=str(N)  # declear a list of str
    dl = []
    nd = len(dc)
    for i in range(nd):
        n=int( dc[i:]+ dc[:i] )  # correct: dc[:0]  ==> []
        if n>10**(nd-1):
           dl.append( n )
    # filterout the element by del, or just do not append it to list
    return set(dl)  # not sorted 

import itertools
def pandigital(N=10):
    d=[str(i) for i in range(N)]
    #d='0123456789'
    l=tuple_iter_to_int_list( itertools.permutations(d,N) ) #  itertools return/yield a iterator  not a list!
    #print l[0], l[-1]
    #filtered out all begins with zero, which should be below 10**9
    list=[i for i in l if i>10**(N-1)]   
    return list

def production(l):
    if len(1)<1:
        return 0
    else:
        r=1
        for i in l:
            r*=i
        return r
        
##############################################################
def all_perms(str):
    """# Python permutation and combination lib? yes, since itertool in v2.6 """
    if len(str) <=1:
        yield str
    else:
        for perm in all_perms(str[1:]):
            for i in range(len(perm)+1):
                yield perm[:i] + str[0:1] + perm[i:]


def combinations_with_replacement(iterable, r):
    # combinations_with_replacement('ABC', 2) --> AA AB AC BB BC CC
    # itertools.combinations_with_replacement(p,r) # no such method for python 2.6, so copy from python.org 
    pool = tuple(iterable)
    n = len(pool)
    if not n and r:
        return
    indices = [0] * r
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != n - 1:
                break
        else:
            return
        indices[i:] = [indices[i] + 1] * (r - i)
        yield tuple(pool[i] for i in indices)

def tuple_list_to_int_list(tl):
    s=[]  #list,  how to declear an empty set?
    for j in tl: 
        # permutations : NO repeated
        number=''
        for c in j :
            number=number+str(c)
        s.append(int(number))
    return s
    
    # all python index begin with zero

tuple_iter_to_int_list=tuple_list_to_int_list            
##############################################################
# for unidirectional increasing func,  arc line searching, x=f_reverse(fx)
def newton_arc(fx, func, x0=0,step=10):

    #if x0==None: x0=0        #only the optional param is a collection, uisng Nome, not empty collection
    f0=func(x0)
    f1=func(x0+step)
    while fx>f1: 
        x0=x0+step
        step=int( (f1-f0)/step * (fx-f1))
        f0=f1
        f1=func(x0+step)
        
    if fx==f1:   print("exact solution is found as :", x0)
    return x0
