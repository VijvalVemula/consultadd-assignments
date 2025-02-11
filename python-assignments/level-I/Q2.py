"""
2. Write a program that accepts a string as input from the user and
calculates the number of digits and letters.
Input: Hello123
Output: Alphabets: 5 & Number : 3
"""
import json
string = input("Enter a string: ")
data = {
    "nums" : 0,
    "alphabets" : 0
}

for char in string:
    if char.isalpha():
        data["alphabets"] += 1
    if char.isdigit():
        data["nums"] += 1

print(f"Alphabets: {data['alphabets']} & Number : {data['nums']}")

