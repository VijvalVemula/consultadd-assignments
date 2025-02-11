"""
5. Write a Python program to find the factorial of a number using a
for loop
"""

num = int(input("Enter a number: "))
factorial = 1

for num in range(1,num+1):
    factorial *= num

print(f"factorial of {num} : {factorial}")

