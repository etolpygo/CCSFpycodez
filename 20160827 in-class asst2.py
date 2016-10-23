#!/usr/bin/python3

"""
08-27 in-class assignment 2

from the /etc/passwd file, generate usernames
"""

def generateUsernames():
    with open('/etc/passwd') as f:
        for line in f:
            username = line.split(':')[0]
            yield username
            
            

generator = generateUsernames()
for value in generator:
	print(value)
    
    
