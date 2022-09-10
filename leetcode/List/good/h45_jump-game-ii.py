'''
https://leetcode.com/problems/jump-game-ii/description/

Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
    Jump 1 step from index 0 to 1, then 3 steps to the last index.
Note:

You can assume that you can always reach the last index.
'''

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        steps = [0] * len(nums)
        
        # breath search, the first time reach one element assign least step for it
        # from i to j, steps[j] = steps[i] + 1 start from cover, which is the farthest
        # all elements can reach by now.
        cover = 0
        for i, n in enumerate(nums):
            for j in range(cover + 1, min(i + n + 1, len(nums))):
                steps[j] = steps[i] + 1
            cover = max(cover, i + n)
        return steps[-1]
            