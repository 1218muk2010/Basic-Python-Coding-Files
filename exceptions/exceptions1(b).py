
def get_number():
    while True:
        try:
            x = int(input("Enter a number: "))
        except ValueError:
                print("Invalid input. Please enter a valid number.")
        else:
            break
    return x    

def main():
    x = get_number()
    print(f"Thank you for entering a valid number. X = {x}")

main()
