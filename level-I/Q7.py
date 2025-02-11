"""
7. Write a Python program to check if a string is an anagram of
another string.
string1 = "listen", string2 = "silent"
Output: True
"""

string1 = input("Enter string 1: ")
string2 = input("Enter string 2: ")

string1 = string1.replace(" ", "").lower()
string2 = string2.replace(" ", "").lower()

print(sorted(string1) == sorted(string2))
