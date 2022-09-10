'''
https://leetcode.com/problems/smallest-range-ii
https://leetcode.com/articles/smallest-range-ii
Given an array A of integers, for each integer A[i] we need to choose either x = -K or x = K, and add x to A[i] (only once).

After this process, we have some array B.

Return the smallest possible difference between the maximum value of B and the minimum value of B.

 





Example 1:


Input: A = [1], K = 0
Output: 0
Explanation: B = [1]



Example 2:


Input: A = [0,10], K = 2
Output: 6
Explanation: B = [2,8]



Example 3:


Input: A = [1,3,6], K = 3
Output: 3
Explanation: B = [4,6,3]


 

Note:


	1 <= A.length <= 10000
	0 <= A[i] <= 10000
	0 <= K <= 10000




'''
class Solution(object):
    # credit to https://leetcode.com/problems/smallest-range-ii/discuss/173377
    def smallestRangeII(self, A, K):
        A.sort()
        res = A[-1] - A[0]
        for i in range(len(A) - 1):
            big = max(A[-1], A[i] + 2 * K)
            small = min(A[i + 1], A[0] + 2 * K)
            res = min(res, big - small)
        return res

s = Solution()
print s.smallestRangeII(range(9999), 10000)
print s.smallestRangeII([0,10], 2)
        
