#List methods



numbers = [0, 1, 2, 3, 4, 5] #Original list
numbers.append(6) #Adding in 6 at the end of the list
print(numbers) # Output: [0, 1, 2, 3, 4, 5, 6]
print(numbers.count(3)) # Counting the number of times 3 appears in the list. Output: 1
print(numbers.index(4)) # Finding the index of the first occurrence of 4 in the list. Output: 4
print(numbers.reverse()) # Reversing the order of the list. Output: [6, 5, 4, 3, 2, 1, 0]
print(numbers.pop(3)) # Removing the element at index 3 (which is 3) from the list. Output: 3

names = ['Alice', 'Bob', 'Charlie', 'David'] #Original list
names.sort() # Sorting the list in alphabetical order. Output: ['Alice', 'Bob', 'Charlie', 'David']
print(names) # Output: ['Alice', 'Bob', 'Charlie', 'David']
names.remove('Bob') # Removing 'Bob' from the list. Output: ['Alice', 'Charlie', 'David']
print(names) # Output: ['Alice', 'Charlie', 'David']
len(names) # Getting the length of the list. Output: 3
