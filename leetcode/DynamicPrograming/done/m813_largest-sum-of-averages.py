'''
https://leetcode.com/problems/largest-sum-of-averages/description/

We partition a row of numbers A into at most K adjacent (non-empty) groups, then our score is the sum of the average of each group. What is the largest score we can achieve?

Note that our partition must use every number in A, and that scores are not necessarily integers.

Example:
Input: 
A = [9,1,2,3,9]
K = 3
Output: 20
Explanation: 
The best choice is to partition A into [9], [1, 2, 3], [9]. The answer is 9 + (1 + 2 + 3) / 3 + 9 = 20.
We could have also partitioned A into [9, 1], [2], [3, 9], for example.
That partition would lead to a score of 5 + 2 + 6 = 13, which is worse.
 

Note:

1 <= A.length <= 100.
1 <= A[i] <= 10000.
1 <= K <= A.length.
Answers within 10^-6 of the correct answer will be accepted as correct.
'''

class Solution(object):
    def largestSumOfAverages(self, A, K):
        """
        :type A: List[int]
        :type K: int
        :rtype: float
        """
        
        ## my solution is correct, but coding logic is messy!

        dp = [[(0,0,0) for _ in xrange(K)] for _ in xrange(len(A))]

        for i, a in enumerate(A):
            _sum = (dp[i-1][0][0] if i > 0 else 0) + A[i]
            dp[i][0] = (_sum, i+1, _sum)
            for j in xrange(1, min(K, i)):
                lusum, lucount, luacc = dp[i-1][j-1]
                lusum += A[i]

                usum = 0
                if j < i:
                    usum, ucount, uacc = dp[i-1][j]
                    usum += (uacc * ucount + A[i]) / ucount - uacc
                
                dp[i][j] = (lusum, 1, A[i]) if lusum > usum else (usum, ucount, uacc * ucount + A[i])
                print dp
        
        return dp[len(A)-1][K-1][0]

s = Solution()
print s.largestSumOfAverages([9,1,2,3,9], 3)