"""
7. Write a program to construct a dictionary from the two lists
containing the names of students and their corresponding
subjects. The dictionary should map the students with their
respective subjects. Let’s see how to do this using for loops and
dictionary comprehension.
Input: [Sam, Alice, Mona] ,
[Commerce, Science, Computer]
Output: [Sam: Commerce, Alice: Science , Mona: Computer]
"""

import json
students = ["Sam", "Alice", "Mona"]
subjects = ["Commerce", "Science", "Computer"]
dictionary = {
    key : value for (key, value) in zip(students, subjects)
}

print(json.dumps(dictionary, indent = 4))