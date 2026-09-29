"""
This file contains a program where the user will get kicked out of the program if they do not entire appropriate data.
"""

"""
import sys
if len(sys.argv) > 2:
    print("Either you have a middle name or you have too many arguments, please omit middle names")
elif len(sys.argv) == 2:
    print("Hello, my name is, " + sys.argv[1])
elif len(sys.argv) < 2:
    print("Too few passed arguements")

    this code ensures the user types in the appropriate amount of arguments, but never kicks them out if they do not.
"""

import sys
if len(sys.argv) > 1:
    sys.exit("Too many passed arguments")
elif len(sys.argv) ==1:
    print("Hello, my name is, " + sys.argv[1])   #This one is the good one 
elif len(sys.argv) < 1:
    sys.exit("Too few passed arguements")


"""
Sys types we learned so far
sys.argv: A list of command-line arguments passed to the script.
sys.exit(): A function that exits the program and can optionally take an argument to specify the exit status or an error message.
"""
