#!/usr/bin/python3

"""
ex. 
decorate print() such that output is also sent into /tmp/log
under conditions. write username & <50 characters of output

print(booktext)

# adds to /tmp/log:
abrick It was a dark & stormy night..


can then:
$tail -f /tmp/log # to see what everyone in the class is printing

"""
import getpass

logfile = '/tmp/log'

def my_decorator(function):
    def gen_logline(args):
        curr_user = getpass.getuser()
        txt = ' '.join(args)
        txt = txt[:50]
        log_line = curr_user+ ': ' + txt + '\n'
        return log_line
        
    def wrapper(*args):
        log_line = gen_logline(args)
        with open(logfile, "a") as l:
            l.write(log_line)
        function(*args)
    return wrapper
    



print = my_decorator(print)

print('1st things first')
print('this is something longer to see if string truncation works the way i am expecting')
print('several things: ', 'something like this, ', 'another thing, ', 'other things')