'''
https://leetcode.com/problems/contiguous-array
https://leetcode.com/articles/contiguous-array

Given a binary array, find the maximum length of a contiguous subarray with equal number of 0 and 1. 

Example 1:

Input: [0,1]
Output: 2
Explanation: [0, 1] is the longest contiguous subarray with equal number of 0 and 1.



Example 2:

Input: [0,1,0]
Output: 2
Explanation: [0, 1] (or [1, 0]) is a longest contiguous subarray with equal number of 0 and 1.



Note:
The length of the given binary array will not exceed 50,000.
'''

class Solution(object):
    def findMaxLength(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # set acc[i] is the accumulative number from 0 to i
        # if substring number[i+1:j] has equal number of 0 and 1
        # then j - i = 2 (acc[j] - acc[i]), means j - 2 * acc[j] = i - 2 * acc[i]
        # the substr length is j - (i+1) + 1 = j - i 
        # (revision: easier way to calculate the value is to add 1 when meet 1, minute 1 when meet -1
        #  then look back if there is a same value. similar to the problem that m523_continuous-subarray-sum
        #)
        # 
        # we just need to accumulate the number from head to tail, calculate the i - 2 * acc[i]
        # check whether the value exist in hashmap, which contain the least index for value
        # if yes, calculate the substr length, otherwise record it.
        acc, maxLen = 0, 0
        memo = {0:0}
        for i in xrange(len(nums)):
            acc += nums[i]
            value = (i+1) - 2 * acc
            # print i, acc, value, memo
            if value in memo:
                maxLen = max(maxLen, (i+1) - memo[value])
            else:
                memo[value] = i+1
    
        return maxLen

s = Solution()
assert s.findMaxLength([]) == 0
assert s.findMaxLength([0]) == 0
assert s.findMaxLength([1]) == 0
assert s.findMaxLength([0,1]) == 2
assert s.findMaxLength([0,1,0]) == 2
assert s.findMaxLength([1,0,1,0,1]) == 4

assert s.findMaxLength([0,0,0,0,0,0,1]) == 2
assert s.findMaxLength([1,1,1,1,1,1,0]) == 2
assert s.findMaxLength([1,1,1,1,1,1,0,0,0,0,0,0,0,0,0,0,0,1,1,1]) == 12
