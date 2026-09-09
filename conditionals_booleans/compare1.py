x = int(input("What is X? " ))


y = int(input("What is Y? " ))
if x > y:
    print("X is greater than Y")
elif x < y:
    print("X is less than Y")
else:
    print("X is equal to Y")

# If is obivous
# Elif is else if, it means that if the first condition is not true, then check this one. You can have as many elifs as you want.
# Else is the default, it means that if none of the previous conditions are true, then do this. You can only have one else.
