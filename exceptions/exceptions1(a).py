'''
x = int(input("What's X? "))
print(f"x is {x}")

The problem with this code is that the user could type in a non-integer value, causing a ValueError
'''

try:
    x = int(input("What is X? "))
    print(f"x = {x}")
except ValueError:
    print("X is not an integer")

'''
You could also do this
try:
    x = int(input("What is X? "))

except ValueError:
    print("X is not an integer")

else
    print(f"x = {x}")


'''
