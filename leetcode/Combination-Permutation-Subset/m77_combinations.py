'''
https://leetcode.com/problems/combinations
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:


Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]

'''
from collections import deque
class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        ans = []
        def dfs(start, n, k, queue):
            # print start, n, k, queue
            if len(queue) == k:
                # deque operations are faster than []
                # list(deque) is same as queue[:]
                ans.append(list(queue))
                return
            if start > n or n+1 - start + len(queue) < k: return

            for i in xrange(start, n+1):
                queue.append(i)
                dfs(i+1, n, k, queue)
                queue.pop()

        dfs(1, n, k, deque())
        return ans

s = Solution()
print s.combine(1,1)
print s.combine(2,1)
print s.combine(2,2)
print s.combine(4,2)

