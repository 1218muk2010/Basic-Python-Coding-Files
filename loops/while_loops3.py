while True:
    n = int(input("Enter a number: "))
    if n < 0: 
        continue
    elif n == 0:
        break
    else:
        break

'''
This part of the program prompts the user to enter a number. It uses a while loop that will continue indefinitely until it encounters a break statement.
If the user enters a negative number (n < 0), the continue statement is executed, which skips the rest of the loop body and starts the next iteration, prompting the user again.

This code can be further simplified by saying:
while True:
    n = int(input("Enter a number: "))
    if n >=0:
        break
        
'''

for _ in range(n):
    print("What's up?")

'''
_ represents a variable that we don't care about.

In this case, we just want to repeat the print statement n times, and we don't need to use the loop variable for anything else.

It takes the value of n and prints out What's up? n times

'''

'''
This is another version of this code that defines functions:

def main():
    n = get_number()
    what_is_up(n)

def get_number():
    while True:
        n = int(input("Enter a number: "))
        if n >= 0:
            return n 

def what_is_up(n):
    for _ in range(n):
        print("What's up?") 

In this code, you use return instead of break to exit the loop in the get_number function because you want to return the value of n to the main function.

'''
