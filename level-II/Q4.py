"""
4. Given an array of size N. The task is to rotate array by D elements
towards right
Sample Input: arr = [1, 2, 3, 4, 5], D = 2
Sample Output: arr after rotation = [4, 5, 1, 2, 3]
"""
arr = list(map(int, input().split()))
d = int(input())
print(arr[-d : ] + arr[ : -d])