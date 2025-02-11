"""
2. Create a function that takes a list and returns a new list with
unique elements of the first list.
Sample Input: list1 = [1, 2, 2, 3, 4, 4, 5, 5]
Sample Output: list2 = [1, 2, 3, 4, 5]
"""

def unique(nums):
    res = list()
    for num in nums:
        if num not in res:
            res.append(num)
        else:
            continue
    return res

nums = list(map(int, input("Enter numbers (space seperated): ").split()))
print(unique(nums))