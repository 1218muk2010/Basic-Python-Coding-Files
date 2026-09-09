students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"},
    {"name": "Draco", "house": "Slytherin", "patronus": "None"},
    {"name": "Luna", "house": "Ravenclaw", "patronus": "Hare"},
    {"name": "Neville", "house": "Gryffindor", "patronus": None},
]
'''
This is a dictionary in Python, which is a collection of key-value pairs. 
In this case, the keys are the names of students (e.g., "Hermione", "Harry"), and the values are their respective houses (e.g., "Gryffindor", "Slytherin").
'''

for student in students:
#Student reqresents each dictionary in the list of dictionaries called students.
    print(student["name"], student["house"], student["patronus"], sep=", ")
'''

This takes the value of the name from the dictionary and takes the value of the house from the dictionary and prints them out together.
You use a list of dictionaries to store information about multiple students, where each dictionary represents a student and contains their name, house, and patronus as key-value pairs.
Then, you can iterate over the list of dictionaries using a for loop to access and print the information for each student.
In the loop, student takes on the value of each dictionary in the students list during each iteration, and you can access the name and house of each student using the keys "name" and "house" respectively.    
'''
