"""
9. Given an input string, write a function that returns the run
length encoded string for the input string.
For Example:
Input: wwwwaaadebbbbbw
Output: w4a3d1e1b5w1
"""

from collections import Counter
def length_encoded(s):
    if not s:
        return ""
    encoded_str = ""
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            encoded_str += s[i - 1] + str(count)
            count = 1
    encoded_str += s[-1] + str(count)
    return encoded_str

s = input("Enter a string: ")

print(length_encoded(s))















