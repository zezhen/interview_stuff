'''
https://leetcode.com/problems/random-pick-index
Given an array of integers with possible duplicates, randomly output the index of a given target number. You can assume that the given target number must exist in the array.

Note:
The array size can be very large. Solution that uses too much extra space will not pass the judge.

Example:


int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly. Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);

'''
class Solution(object):

    # 1. O(n) space init, O(1) time each pick, hasmap to keep num -> [index], random select from hit index list
    # 2. O(n) time each pick, scan nums, if nums[i] == target, 1/(k+1) probility select

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        

    def pick(self, target):
        """
        :type target: int
        :rtype: int
        """
        


# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)