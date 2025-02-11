"""
6. Write a Python program to check if a given number is a perfect
number.
A Perfect number is a positive integer that is equal to the sum of
its proper divisors. For instance, 6 has divisors 1, 2, and 3, and 1 + 2 +
3 = 6, so 6 is a perfect number.
"""

num = int(input("Enter a number: "))
factors = list(set([fact for fact in range(1, num + 1) if num % fact == 0]))

print("Yes") if ((sum(factors) - num) == num) else print("No")


