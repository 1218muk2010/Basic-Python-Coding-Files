len(set(numbers)) # Output: 6
numbers.add(7) # Adding 7 to the set
print(set(numbers)) # Output: {1, 2, 3, 4, 5, 6, 7}

set1 = {1, 2, 3}
set2 = {3, 4, 5}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5}
print(set1.intersection(set2)) # Output: {3}
set3 = set1.difference(set2) # Output: {1, 2}
print(set3)
allsets = set1.union(set2).union(set3) # Output: {1, 2, 3, 4, 5}
print(allsets)

word = "anitdisestablishmentarianism"
print(len(set(word))) # Output: 12; the number of unique letters in the word
