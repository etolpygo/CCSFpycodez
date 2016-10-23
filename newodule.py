#/usr/local/bin/python3
# Elena Tolpygo Cranley
# 2016-08-28

"""
newmodule, due 8/28: Find a module in the Python Standard Library that you've never seen before and write a skeleton useful program with it
"""

import sys
import statistics

def arg_error():
    print('Please input a list of (space-separated) numbers as arguments.')
    sys.exit()

if len(sys.argv) <= 1:
    arg_error()

sys.argv.pop(0)

try:
    numbers = [ float(x) for x in sys.argv ]
except ValueError:
    arg_error()

print('Mean(average) of arguments is: ', statistics. mean(numbers))
print('Median (middle value) of arguments is :', statistics.median(numbers))
print('Variance of the data is: ', statistics.variance(numbers))
print('Standard deviation of the data is: ', statistics.stdev(numbers))