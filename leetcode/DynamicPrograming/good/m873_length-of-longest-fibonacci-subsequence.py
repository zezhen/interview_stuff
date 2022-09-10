'''
https://leetcode.com/problems/length-of-longest-fibonacci-subsequence/description/

A sequence X_1, X_2, ..., X_n is fibonacci-like if:

n >= 3
X_i + X_{i+1} = X_{i+2} for all i + 2 <= n
Given a strictly increasing array A of positive integers forming a sequence, find the length of the longest fibonacci-like subsequence of A.  If one does not exist, return 0.

(Recall that a subsequence is derived from another sequence A by deleting any number of elements (including none) from A, without changing the order of the remaining elements.  For example, [3, 5, 8] is a subsequence of [3, 4, 5, 6, 7, 8].)

 

Example 1:

Input: [1,2,3,4,5,6,7,8]
Output: 5
Explanation:
The longest subsequence that is fibonacci-like: [1,2,3,5,8].
Example 2:

Input: [1,3,7,11,12,14,18]
Output: 3
Explanation:
The longest subsequence that is fibonacci-like:
[1,11,12], [3,11,14] or [7,11,18].
 

Note:

3 <= A.length <= 1000
1 <= A[0] < A[1] < ... < A[A.length - 1] <= 10^9
(The time limit has been reduced by 50% for submissions in Java, C, and C++.)
'''

class Solution(object):
    def lenLongestFibSubseq_dp(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        def search_2sum(A, end, target):
            l, r = 0, end
            ans = []
            while l < r:
                if A[l] + A[r] == target:
                    ans.append((l, r))
                    l += 1
                    r -= 1
                elif A[l] + A[r] > target:
                    r -= 1
                else:
                    l += 1
            return ans

        length = len(A)
        # set dp[n][m] as the length of longest fibonacci-like subsequence 
        # that ends with A[m] and A[n], so dp[n][m] = d[x][m] + 1
        # given index n, we can use search_2sum function to find all (m,x) that meet
        # A[m] + A[x] = A[n], then max(A[n][*]) is the answer.
        # set default value as 2 if valid, need to check the max(*) at last step, 
        # if size is 2, it menas no fibonacci-like subsequence exist.
        dp = [[2 for _ in range(length)] for _ in range(length)]
        if A[0] + A[1] == A[2]:
            dp[2][1] = 3
        
        for i in range(3, len(A)):
            _2sum_index = search_2sum(A, i, A[i])
            for l, r in _2sum_index:
                dp[i][r] = dp[r][l] + 1
        
        size = max(map(max, dp))
        return size if size > 2 else 0
                
    def lenLongestFibSubseq_hash(self, A):
        s = set(A)
        res = 2
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                a, b, l = A[i], A[j], 2
                while a + b in s:
                    a, b, l = b, a + b, l + 1
                res = max(res, l)
        return res if res > 2 else 0
            