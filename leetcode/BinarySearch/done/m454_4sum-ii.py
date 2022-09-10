'''
https://leetcode.com/problems/4sum-ii/description/

Given four lists A, B, C, D of integer values, compute how many tuples (i, j, k, l) there are such that A[i] + B[j] + C[k] + D[l] is zero.

To make problem a bit easier, all A, B, C, D have same length of N where 0 <= N <= 500. All integers are in the range of -2^28 to 2^28 - 1 and the result is guaranteed to be at most 2^31 - 1.

Example:

Input:
A = [ 1, 2]
B = [-2,-1]
C = [-1, 2]
D = [ 0, 2]

Output:
2

Explanation:
The two tuples are:
1. (0, 0, 0, 1) -> A[0] + B[0] + C[0] + D[1] = 1 + (-2) + (-1) + 2 = 0
2. (1, 1, 0, 0) -> A[1] + B[1] + C[0] + D[0] = 2 + (-1) + (-1) + 0 = 0
'''

import collections
class Solution(object):
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        AB_sum = collections.defaultdict(int)
        for i,a in enumerate(A):
            for j,b in enumerate(B):
                plus = a + b
                AB_sum[plus] += 1
        
        ans = 0
        for i,c in enumerate(C):
            for j,d in enumerate(D):
                target = - (c + d)
                ans += AB_sum[target]
                
        return ans


import random
A = [random.randint(-1000, 1000) for _ in xrange(200)]
B = [random.randint(-1000, 1000) for _ in xrange(200)]
C = [random.randint(-1000, 1000) for _ in xrange(200)]
D = [random.randint(-1000, 1000) for _ in xrange(200)]

print A
print B
print C
print D

s = Solution()
print s.fourSumCount(A, B, C, D)
