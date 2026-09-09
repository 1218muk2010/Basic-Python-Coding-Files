while True:
    try:
        x = int(input("Enter a number: "))
    except ValueError:
        print("Invalid input. Please enter a valid number.")
    else:
        break

print(f"Thank you for entering a valid number. X = {x}") 



'''
You could also do this

while True:
    try:
        x = int(input("Enter a number: "))
        break
    except ValueError:
        print("Invalid input. Please enter a valid number.")
print(f"Thank you for entering a valid number. X = {x}")

'''
