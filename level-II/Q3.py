"""
3. Given an array of N integers and an integer K, find the number of
pairs of elements in the array whose sum is equal to K.
Sample Input: arr = [1, 2, 3, 4, 5], k = 6
Sample Output: Pair count: 2
"""

nums = list(map(int, input().split()))
k = int(input())

count = 0
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == k:
            count += 1
print(count)