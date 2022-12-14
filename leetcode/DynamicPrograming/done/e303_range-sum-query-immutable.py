'''
https://leetcode.com/problems/range-sum-query-immutable
https://leetcode.com/articles/range-sum-query-immutable
Given an integer array nums, find the sum of the elements between indices i and j (i <= j), inclusive.

Example:

Given nums = [-2, 0, 3, -5, 2, -1]

sumRange(0, 2) -> 1
sumRange(2, 5) -> -1
sumRange(0, 5) -> -3



Note:

You may assume that the array does not change.
There are many calls to sumRange function.

'''

'''
acc[i] = sum(nums[:i])
sumRange(i,j) = acc[j] - (acc[i-1] if i>0 else 0)
'''