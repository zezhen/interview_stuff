'''
https://leetcode.com/problems/partition-equal-subset-sum/description/

Given a non-empty array containing only positive integers, find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.

Note:
Each of the array element will not exceed 100.
The array size will not exceed 200.
Example 1:

Input: [1, 5, 11, 5]

Output: true

Explanation: The array can be partitioned as [1, 5, 5] and [11].
Example 2:

Input: [1, 2, 3, 5]
 
Output: false

Explanation: The array cannot be partitioned into equal sum subsets.
'''

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        _sum = sum(nums)
        if len(nums) <= 1 or _sum % 2 != 0: return False

        target = _sum / 2

        '''
        by now the problem becomes to tell whether we can find a subarray that it's sum is equal to target.
        1. order the array and solve it 0/1 knapsack way, use memo to maintain duplicated sub-space.
        2. dp[i][j] means whether the specific target j can be gotten from the first i numbers
            dp[0][0] = true,
            dp[i][j] = dp[i-1][j] || (dp[i-1][j - nums[j]] if j > nums[j] else False)

        cons: 1 is the time, 2 is the space
        '''
