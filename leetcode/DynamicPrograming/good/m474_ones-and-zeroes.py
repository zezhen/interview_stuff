'''
https://leetcode.com/problems/ones-and-zeroes/description/

In the computer world, use restricted resource you have to generate maximum benefit is what we always want to pursue.

For now, suppose you are a dominator of m 0s and n 1s respectively. On the other hand, there is an array with strings consisting of only 0s and 1s.

Now your task is to find the maximum number of strings that you can form with given m 0s and n 1s. Each 0 and 1 can be used at most once.

Note:
The given numbers of 0s and 1s will both not exceed 100
The size of given string array won't exceed 600.
Example 1:
Input: Array = {"10", "0001", "111001", "1", "0"}, m = 5, n = 3
Output: 4

Explanation: This are totally 4 strings can be formed by the using of 5 0s and 3 1s, which are "10,"0001","1","0"
Example 2:
Input: Array = {"10", "0", "1"}, m = 1, n = 1
Output: 2

Explanation: You could form "10", but then you'd have nothing left. Better form "0" and "1".
'''

class Solution(object):

    '''
    my solution as below is to use DP to solve the problem, space is a problem, low efficiency

    Greedy solution works for this problem, order strs by (zeros, ones), two for-loop to check

    '''
    def findMaxForm_dp(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def count(s):
            ones = 0
            for c in s:
                if c == '1': ones += 1
            return ones, len(s) - ones

        dp = [ [ [0 for _ in xrange(n+1)] for _ in xrange(m+1) ] for _ in xrange(len(strs)+1)]

        for i in xrange(1, len(strs) + 1):
            ones, zeros = count(strs[i-1])
            for j in xrange(m+1):
                for k in xrange(n+1):
                    if j >= zeros and k >= ones:
                        dp[i][j][k] = max(dp[i-1][j-zeros][k-ones] + 1, dp[i-1][j][k])
                    else:
                        dp[i][j][k] = dp[i-1][j][k]
                        
        # print dp
        return dp[len(strs)][m][n]

    def findMaxForm(self, strs, m, n):
    	return self.findMaxForm_dp(strs, m, n)

    def findMaxForm_greedy(self, strs, m, n):
        """
        :type strs: List[str]
        :type m: int
        :type n: int
        :rtype: int
        """
        def count(s):
            ones=zeros=0
            for x in s:
                if x=='0':
                    zeros+=1
                else:
                    ones+=1
            return zeros, ones
        ans=0
        L=len(strs)
        matrix=[count(s) for s in strs]
        matrix.sort()
        print matrix
        for i in range(L):
            zeros, ones = matrix[i]
            if ones > n or zeros>m:
                continue
            cur=1
            for j in range(i+1,L):
                z,o=matrix[j]
                if ones+o<= n and zeros+z<=m:
                    ones+=o
                    zeros+=z
                    cur+=1
            ans=max(ans,cur)

        return ans


s = Solution()
assert s.findMaxForm([], 3, 4) == 0
assert s.findMaxForm(['1','1'], 0, 0) == 0
assert s.findMaxForm(['0','1'], 1, 0) == 1
assert s.findMaxForm(['0','1'], 0, 1) == 1
assert s.findMaxForm(['1','1'], 3, 4) == 2
assert s.findMaxForm(['1','11', '10', '0'], 1, 4) == 3
assert s.findMaxForm(["10", "0001", "111001", "1", "0"], 5, 3) == 4
assert s.findMaxForm(["10", "0", "1"], 1, 1) == 2

assert s.findMaxForm(["1110", "0001","001"], 6, 3) == 2

