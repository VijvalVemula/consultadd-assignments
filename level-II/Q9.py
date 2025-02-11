"""
9. Write a Python program that executes an operation on a list and
handles an IndexError exception if the index is out of range.
"""

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]


while True:
    try:
        print(nums[int(input("Enter an index: "))])
        break
    except IndexError as e:
        print(f"There is an index error: {e}. Please enter a valid index.")
        print(f"Number must be less than {len(nums)}")