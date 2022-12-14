'''
https://leetcode.com/problems/top-k-frequent-elements
Given a non-empty array of integers, return the k most frequent elements.

Example 1:


Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]



Example 2:


Input: nums = [1], k = 1
Output: [1]


Note: 


	You may assume k is always valid, 1 <= k <= number of unique elements.
	Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

'''
import heapq
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        
        _dict = {}
        for n in nums:
            _dict[n] = (_dict[n] if n in _dict else 0) + 1

        topk = []
        for num,count in _dict.iteritems():
            heapq.heappush(topk, (-count, num))

        return map(lambda t: t[1], heapq.nsmallest(k, topk))