'''
https://leetcode.com/problems/factor-combinations

Numbers can be regarded as product of its factors. For example,

8 = 2 x 2 x 2;
  = 2 x 4.
Write a function that takes an integer n and return all possible combinations of its factors.

Note:

You may assume that n is always positive.
Factors should be greater than 1 and less than n.
Example 1:

Input: 1
Output: []
Example 2:

Input: 37
Output:[]
Example 3:

Input: 12
Output:
[
  [2, 6],
  [2, 2, 3],
  [3, 4]
]
Example 4:

Input: 32
Output:
[
  [2, 16],
  [2, 2, 8],
  [2, 2, 2, 4],
  [2, 2, 2, 2, 2],
  [2, 4, 4],
  [4, 8]
]
'''

import math
class Solution(object):
    cache = {}

    def getFactors(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n in self.cache:
            return self.cache[n]

        ans = []
        for i in xrange(2, int(math.sqrt(n))+1):
            if n % i != 0: continue
            ans.append([i, n/i])
            res = self.getFactors(n/i)
            for r in res:
                if i > r[0]: continue
                ans.append([i] + r)

        self.cache[n] = ans
        return ans

s = Solution()
print s.getFactors(1)
print s.getFactors(2)
print s.getFactors(4)
print s.getFactors(6)
print s.getFactors(8)
print s.getFactors(12)

