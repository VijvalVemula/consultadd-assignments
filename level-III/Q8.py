"""
8. You need to write a function that accepts an encoded string as a
parameter.
This string will contain a first name, last name, and an id.
Values in the string can be separated by any number of zeros. The
id is a numeric value but will contain no zeros. The function should
parse the string and return a Python dictionary that contains the
first name, last name, and id values.
For example:
Input : “Robert000Smith000123”
Output:
{ “first_name”: “Robert”, “last_name”: “Smith”, “id”: “123” }
"""

def parse_string(string):
    words = [word for word in string.split("0") if word != ""]
    if len(words) == 3:
        data = {
            "first_name": words[0],
            "last_name": words[1],
            "id": words[2]
        }
    else:
        raise ValueError("Invalid Input")
    return data

string = input("Enter the string: ")
print(parse_string(string))