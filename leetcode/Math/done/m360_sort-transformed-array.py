'''
https://leetcode.com/problems/sort-transformed-array

Given a sorted array of integers nums and integer values a, b and c. Apply a quadratic function of the form f(x) = ax^2 + bx + c to each element x in the array.

The returned array must be in sorted order.

Expected time complexity: O(n)

Example 1:

Input: nums = [-4,-2,2,4], a = 1, b = 3, c = 5
Output: [3,9,15,33]
Example 2:

Input: nums = [-4,-2,2,4], a = -1, b = 3, c = 5
Output: [-23,-5,1,7]
'''

class Solution(object):
    def sortTransformedArray(self, nums, a, b, c):
        """
        :type nums: List[int]
        :type a: int
        :type b: int
        :type c: int
        :rtype: List[int]
        """

        # the mid of form f(x) is - b / 2a, the if a > 0, mid is minimum, otherwise maximum
        # binary search the index of mid in sorted array nums
        # for l and r, check distance between nums[l] and nums[r] to mid