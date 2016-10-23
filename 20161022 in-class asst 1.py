#!/usr/bin/python3

""" 
python3 prog.py BBCC 45.2 34

ex 1:
comprehension:
output the square roots of all command line arguments that are positive integers

ex 2:
map/filter only:
same as above, but output the least of those square roots
"""

import sys, math

    
args = sys.argv[1:]

square_roots = list(map(lambda x: math.sqrt(x), map(int, filter(lambda a: a.isdigit(), args))))

print(square_roots)

print(min(square_roots))