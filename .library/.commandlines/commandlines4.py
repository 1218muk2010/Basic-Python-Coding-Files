#Using or accessing parts or "slices" of data

import sys

if len(sys.argv) > 2:
    sys.exit("You have too many arguments")

for arg in sys.argv [1:]:  #This is the slice of the list that we want to access, which is all the arguments except the first one (the name of the file).
    print("Hello, my name is, " + arg)

"""This takes out the first value in the inputted list given by the user, which is the file name, and then prints out 
all other values in the list. THe space means that it is going on until the end of the list, so it will print out all the names that the user inputs."""

