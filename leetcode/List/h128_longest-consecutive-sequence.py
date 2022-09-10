'''
https://leetcode.com/problems/longest-consecutive-sequence/description/

Given an unsorted array of integers, find the length of the longest consecutive elements sequence.

Your algorithm should run in O(n) complexity.

Example:

Input: [100, 4, 200, 1, 3, 2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

'''

import collections
class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        p = range(len(nums))
        _map = dict(map(lambda (i,n):(n,i), enumerate(nums)))

        def pid(_id):
            while _id != p[_id]:
                p[_id] = p[p[_id]]
                _id = p[_id]
            return _id

        for i,n in enumerate(nums):
            for t in [n-1, n+1]:
                if t in _map:
                    x = pid(_map[n])
                    y = pid(_map[t])

                    if x != y:
                        p[_map[t]] = x
        for i in xrange(len(nums)):
            pid(i)

        count = collections.Counter(p)
        return count.most_common(1)[0][1]

s = Solution()
print s.longestConsecutive([100, 4, 200, 1, 3, 2]) == 4
print s.longestConsecutive([4, 6, 1, 7, 3, 10, 9, 2]) == 4

