name = input("What is your name? ")

match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco"  | "Crabbe" | "Goyle":
        print("Slytherin")
    case "Luna" | "Cho" | "Padma":
        print("Ravenclaw")
    case "Cedric" | "Hannah" | "Ernie":
        print("Hufflepuff")
    case _:
        print("That is not a valid name, try again.")

'''
Match statements are a powerful tool for handling multiple cases in a clean and readable way. 
In this code, we are using a match statement to determine which Hogwarts house a person belongs to based on their name.

The lines that start with "case" are the different cases that we are checking for.
For example, the first case checks if the name is "Harry", "Hermione", or "Ron".
If the name matches any of those, it will print "Gryffindor

'''
