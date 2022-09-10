'''
https://leetcode.com/problems/subarray-sum-equals-k
https://leetcode.com/articles/subarray-sum-equals-k

Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

Example 1:

Input:nums = [1,1,1], k = 2
Output: 2



Note:

The length of the array is in range [1, 20,000].
The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].


'''
import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        '''
        my first solution is quite complicated, 
        later I come up with accumulate + hashmap(acc -> count),
        but there is one problem, for position i, target = k - acc[i], when checking in hashmap
        the hit number could be before or after j, should I change hashmap to acc->[position list] then binary search?
        that's make thing complicated again.
        until checking others' solution is to use presum, which means accumulating and checking happen same time.
        '''
        count = collections.defaultdict(int)
        ans, acc = 0, 0

        count[acc] = 1
        for i in xrange(len(nums)):
            acc += nums[i]
            target = acc - k
            if target in count:
                ans += count[target]
            count[acc] += 1
        
        return ans
            
s = Solution()
assert s.subarraySum([], 3) == 0
assert s.subarraySum([1,1,1], 0) == 0
assert s.subarraySum([1,1,1], 2) == 2
assert s.subarraySum(range(-1000, 1000), 10) == 4
