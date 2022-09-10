'''
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii
https://leetcode.com/articles/minimum-moves-to-equal-array-elements-ii
Given a non-empty integer array, find the minimum number of moves required to make all array elements equal, where a move is incrementing a selected element by 1 or decrementing a selected element by 1.

You may assume the array's length is at most 10,000.

Example:

Input:
[1,2,3]

Output:
2

Explanation:
Only two moves are needed (remember each move increments or decrements one element):

[1,2,3]  =>  [2,2,3]  =>  [2,2,2]

'''
class Solution(object):
    def minMoves2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # refer to https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/discuss/94937/

        nums.sort()
        return sum(nums[~i] - nums[i] for i in range(len(nums) / 2))


        # we need find some mid point x to make all numbers move there.
        # sorted numbers, min is nums[0], max is nums[n-1]
        # nums[0] <= x <= nums[n-1]
        # moves = (x - nums[0]) + (nums[n-1] - x) = nums[n-1] - nums[0]
        # independent of x


        # if we choose other x, like x > nums[n-1] or x < nums[0]
        # moves will be greater than nums[n-1] - nums[0] obviously

        # thus we need to choose x meet that nums[i] <= x <= nums[n-1-i]
        # thus we need to choose the median number