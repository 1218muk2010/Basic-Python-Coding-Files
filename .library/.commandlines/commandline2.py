"""
Using an exception in the sys.argv variable if no value is inputed

""" 

import sys
try:
    print("Hello, my name is, " + sys.argv[1])
except IndexError:
    print("You forgot to input a name")


"""
Other version of the code

import sys
if len(sys.argv) > 1: 
    print("Hello, my name is, " + sys.argv[1])
else:
    print("You forgot to input a name")

On this one, it makes sure that the length of the sys.argv list is greater than 1, which means that there is at least one argument passed in (the name). If there is an argument, it prints the greeting. If there isn't, it prints the error message.
"""
