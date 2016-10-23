#!/usr/bin/python3

"""
08-27 in-class assignment 3

write a generator of prime numbers

"""

import math

def primeGen():
    a = 2
    while True:
        if is_prime(a):
            yield a
        a += 1
    
    
        
def is_prime(number):
    if number > 1:
        if number == 2:
            return True
        if number % 2 == 0:
            return False
        for current in range(3, int(math.sqrt(number) + 1), 2):
            if number % current == 0:
                return False
        return True
    return False

        
generator = primeGen()
for x in range(1000):
    print(next(generator))


    