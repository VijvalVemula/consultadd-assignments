"""
2. Write a program to count the lines in a file “demo.txt”
"""
with open("demo.txt", mode ="r") as file_handle:
    lines = file_handle.readlines()

print(len(lines))