animals = ["cat", "dog", "rabbit"]

print(animals[0]) 
#Output: cat

''' 
print(animals[1])  # Output: dog
print(animals[2])  # Output: rabbit

A more advanced version of this code:

animals = ["cat", "dog", "rabbit"]

for animal in animals:
    print(animal)

You could also use integers to loop through the list:

animals = ["cat", "dog", "rabbit"]
for i in range(len(animals)):
    print(animals[i])

If you were to rank the animals, you could apply the same logic:
animals - ["cat", "dog", "rabbit"]
for i in range(len(animals)):
    print(f"{i + 1}. {animals[i]}")

If you were to reverse the order of the animals, you could do:
animals = ["cat", "dog", "rabbit"]
for i in range(len(animals)-1, -1, -1):
    print(animals[i])

'''
