# -*- coding: utf-8 -*-
from __future__ import print_function, unicode_literals, absolute_import, division
"""
	problem 12  Starting in the top left corner of a 2X2 grid, there are 6 routes 
	(without backtracking) to the bottom right corner.
	How many routes are there through a 20X20 grid?    
	Solu:  recursive, the recursion depth of python?  can not do 20X20?
	the stack of recursion is 2**19, it is too big even if sys.setrecursionlimit(limit)
"""

def grid_path(row, col):
	""" this is a general method, but row can not exceed 10, or
	RuntimeError: maximum recursion depth exceeded"""
	#if(col<0 and row<0):
	#	print "col row dest should be bigger than 0"
	#	return
	if(row ==0 or col==0):  # same row/col, has only one choice
		return 1
		#
	choice=0
	choice = grid_path(row-1,col) + grid_path(row,col-1)
	return choice
	# end
def calc_grid_path():
	c=grid_path(20,20)
	print("the 20X20 grid move choice is:", c)
	#
	
def diag_divide(row, col):
	"""  the pass can only pass the diag element once, and it is square,
	this is a symmetrical problem,  for a square with even row count
	since grid 10X10 is 184756 can be calculate very quick, decrease the problem into half """
	ways =0
	if(row == col  and  row%2==0):
		cn = grid_path(row/2, row/2)
		ways += cn * cn  # centre of grid
		for i in range(1,int(row/2)+1):
			mn = grid_path(row/2+i, row/2-i)
			ways += 2* mn *mn
	else:
		print(" it need to be a square with even row count")
	return ways
	
def main():
	#timeit is import from helper, instead of timeit module
	from sys import setrecursionlimit
	limit = 1000000
	setrecursionlimit(limit)
	#timeit(calc_grid_path)
	#print "the 2X2 grid move choice is:", timeit(grid_path,2,2)
	print("the 20X20 grid move choice is:", diag_divide(20,20))
	#wait=raw_input("wait any key to eixt")
if __name__ == "__main__":
    main()