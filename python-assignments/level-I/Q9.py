"""
9. Write a Python program to count the frequency of each element
in a list.
Input_list = [1, 2, 3, 2, 4, 1, 2, 4, 5]
Frequency count: {1: 2, 2: 3, 3: 1, 4: 2, 5: 1}
"""

nums = list(map(int, input("Enter numbers (space seperated): ").split()))
counts = dict()

for num in nums:
    if num in counts.keys():
        counts[num] += 1
    else:
        counts[num] = 1

print(f"Frequency count: {counts}")
