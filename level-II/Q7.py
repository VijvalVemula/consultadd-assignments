"""
7. Write a Python function that finds the median of a list of
numbers.
Sample Input: number_list = [7, 2, 5, 1, 9, 3]
Sample Output: Median: 4.0
"""

def find_median(number_list):
    number_list.sort()
    n = len(number_list)

    if n % 2 == 1:
        return number_list[n // 2]
    else:
        mid1 = number_list[n // 2 - 1]
        mid2 = number_list[n // 2]
        return (mid1 + mid2) / 2

number_list = list(map(int, input("Enter list space seperated: ").split()))
median = find_median(number_list)
print("Median:", median)
