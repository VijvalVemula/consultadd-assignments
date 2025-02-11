"""
10. Write a Python program to reverse the order of words in a given
sentence.
Input_sentence = “Hello, World! Welcome to Python programming.”
Output after reverse = “programming. Python to Welcome World! Hello,”
"""

sentence = input("Enter the sentence you want to reverse: ")

tokens = sentence.split(" ")

reversed_tokens = tokens[ : : -1]
reversed_sentence = " ".join(reversed_tokens)
print(reversed_sentence)
