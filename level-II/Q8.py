"""
8. Write a Python function that counts the number of vowels in a
given string.
Sample Input: string = "Hello, World!"
Sample Output: Number of vowels: 3
"""

def count_vowels(sentence):
    vowels = ["a", "e", "i", "o", "u"]
    count = 0
    for char in sentence:
        if char in vowels:
            count += 1
    return count

sentence = input("Enter a sentence: ")
print(count_vowels(sentence))