"""
11. Write a Python program to calculate the sum of digits of a given
number until the sum becomes a single-digit number.
Sample Input: num = 987
Sample Output: Sum_of_digits = 24,
Again compute the sum of digits so that it can be reduced to
on single digit.
Final Output: 6
"""

num = int(input("Enter a number: "))
digits = lambda n : len(str(n))

while num >= 10:
    total = 0
    sum_digits = 0
    while num > 0:
        sum_digits += num % 10
        num //= 10
    num = sum_digits

print(num)


