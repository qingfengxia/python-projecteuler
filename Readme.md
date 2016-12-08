
## Why I solve problems on projecteuler

practice math and algorithms

## Why I choose python?

+ Built-in support:  BigInt Decimal, Set Permutations and Combinations 
+ Compact coding:    one line to solve some problems in python, for most of problems below 100, less than 50 lines are enough to solve

Python2 is used to solve the problems before 2013. `2to3 -w -f print thisfile.py` has converted the code into python2 and python3 compatible in 2016, replacing print keyword into print_function

## Strategy 

as shown in `projectEuler_template.py`

Firstly, try bruteforce, which is logically evidently and intuitive;  Then, test it by the example data given by problem description. After that, try to solve the problem, if it does not give you an answer in 3 minutes. Try some smarter approaches.

## What I have done?

I prepared some utility methods to accelerate computation

```python
prime.py

facterization.py

fabonacci.py

projecteulerhelper.py    # generate list for circular number, pandigital, etc

projectEuler_template.py  # template for test-driven programming modeltimeit.py
```

some poker games

```python
twentyfour_poker.py
TexasHoldemPoker.py
card.py
```

they are compatible to python2 and python3.


## progress

- most of problems up to problem 50 are solved
- 33, 55,85, 58, 67 no  solution implemented
- 31, 44, 50, 59: bruteforce failed

---------------------------------------------
- 60 to 100: only a few problems are tried
- 71 not correct
- 60, 70, 81, 100 failed to find a solution by bruteforce

---------------------------------------------
need further optimization, e.g.  cython
- 51 takes 25 second to finish by bruteforce
- 40 takes 171 seconds to finish by bruteforce
- 43 takes 30 seconds to finish by bruteforce

## todo

- test on python3
- clean up code
- problems 55 and 85 are not solved 

## see also other authors's website

more than 200 problems solved by Java 	Python 	Mathematica 	Haskell: <https://github.com/nayuki/Project-Euler-solutions>

60 problems: <http://www.s-anand.net/euler.html>
   
## Source code Licensed under BSD license

The source codes are provided for problems I solved:

but it is recommended that you try your thought and code first.
If your code does not work, have a look of my code or search the intermet.  In my case, I will never search codes to solve problems before I try my best.