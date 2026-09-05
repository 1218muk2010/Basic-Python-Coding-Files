x = float(input("what is x? "))
y = float(input("what is y? "))

z = round(x + y, 0)



'''
print(round(float(x) + float(y), 8))

this eight shows how many decimal places you want to round to. 
You can change it to any number you want. 
If you want to round to the nearest whole number, you can use 0. 
'''

# this code shows how to add commas

print(f"{z:,}")
# remember to use f strings when using commas,
# and the : is used to specify that we want to use commas in our output.
