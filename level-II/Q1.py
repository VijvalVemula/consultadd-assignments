"""
1. Write a Python program to find the common elements between
two lists.
Sample Input: l1 = [1, 2, 3, 4, 5] and l2 = [4, 5, 6, 7, 8]
Sample output: [4, 5]
"""

nums1 = list(map(int, input("Enter list1 (space seperated): ").split()))
nums2 = list(map(int, input("Enter list2 (space seperated): ").split()))

common = list()

for num in nums1:
    if num in nums2 and num not in common:
        common.append(num)


print(common)