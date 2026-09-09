x={1,2,3}
y={2,3,4}
print(x.difference(y).union(y.difference(x))) # Output: {1, 4}; the elements that are in either x or y but not in both

#You could also use the symmetric_difference method to achieve the same result
print(x.symmetric_difference(y)) # Output: {1, 4}
#Lastly, you could use the caret operator (^) to achieve the same result
print(x^y) # Output: {1, 4}

print(x.issubset(y)) # Output: False; x is not a subset of y
print(x.issuperset(y)) # Output: False; x is not a superset of y
