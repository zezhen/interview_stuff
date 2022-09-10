'''
https://leetcode.com/problems/4-keys-keyboard
https://leetcode.com/articles/4-keys-keyboard

Imagine you have a special keyboard with the following keys:

Key 1: (A): Print one 'A' on screen.

Key 2: (Ctrl-A): Select the whole screen.

Key 3: (Ctrl-C): Copy selection to buffer.

Key 4: (Ctrl-V): Print buffer on screen appending it after what has already been printed.

Now, you can only press the keyboard for N times (with the above four keys), find out the maximum numbers of 'A' you can print on screen.

Example 1:

Input: N = 3
Output: 3
Explanation: 
We can at most get 3 A's on screen by pressing following key sequence:
A, A, A
Example 2:

Input: N = 7
Output: 9
Explanation: 
We can at most get 9 A's on screen by pressing following key sequence:
A, A, A, Ctrl A, Ctrl C, Ctrl V, Ctrl V
Note:

1 <= N <= 50
Answers will be in the range of 32-bit signed integer.
'''
class Solution(object):
    def maxA(self, N):
        """
        :type N: int
        :rtype: int
        """

        # use i steps to reach maxA(i) 
        # then use the remaining n - i steps to reach n - i - 1 copies of maxA(i)
        dp = [0] * (N+1)
        for i in xrange(N+1):
            dp[i] = i
            for j in xrange(i-2):
                dp[i] = max(dp[i], dp[j] * (i-j-1))
        
        return dp[N]
    
    def maxA_dfs(self, N):
        memo = {}
        def dfs(footprint, x, ctrlv):
            if x <= 0: return footprint
            if (footprint, x, ctrlv) in memo: 
                return memo[(footprint, x, ctrlv)]
        
            ans = dfs(footprint + ctrlv, x - 1, ctrlv) if ctrlv else dfs(footprint + 1, x-1, '')
            ans = max(ans, dfs(footprint * 2, x - 3, footprint) if x >= 3 else 0)
            memo[(footprint, x, ctrlv)] = ans
            return ans

        return dfs(0, N, '')



s = Solution()
# print s.maxA(3) == 3
# print s.maxA(7) == 9
# print s.maxA(17) == 144
# print s.maxA(21) == 432
print s.maxA(49) == 1048576