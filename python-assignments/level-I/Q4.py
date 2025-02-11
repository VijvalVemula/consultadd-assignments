"""
4. Write a Python program to find the sum of all odd numbers
between two given numbers.
Start = 1, stop = 10
Sum of odd numbers: 25
"""
sum = 0
start = int(input("Enter the starting number: "))
stop = int(input("Enter the stop number: "))
for num in range(start, stop+1):
    if num % 2 != 0:
        sum += num
print(f"sum of odds: {sum}")
