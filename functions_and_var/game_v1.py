def get_guess():
    guess = int(input("What is your guess? "))
    return guess

def main():
    print("Welcome to the guessing game!")
    print("I am thinking of a number between 1 and 10.")
    guess = get_guess()
    if guess == 5:
        print("Congratulations! You guessed the correct number.")
    else:
        print("Sorry, that's not the correct number. Try again!")

main()
