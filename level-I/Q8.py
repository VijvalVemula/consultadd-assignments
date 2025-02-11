"""
8. Write a Python program to calculate the LCM (Least Common
Multiple) of two numbers.
number1 = 12, number2 = 18
LCM of 12 and 18 are: 36
"""

a, b = list(map(int, input("Enter two numbers space seperated: ").split()))

greater = max(a, b)

while True:
    if (greater % a == 0) and (greater % b == 0):
        print(f"LCM of {a} and {b} is {greater}")
        break
    greater += 1

