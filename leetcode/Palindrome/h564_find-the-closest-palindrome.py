'''
https://leetcode.com/problems/find-the-closest-palindrome/description/

Given an integer n, find the closest integer (not including itself), which is a palindrome.

The 'closest' is defined as absolute difference minimized between two integers.

Example 1:
Input: "123"
Output: "121"
Note:
The input n is a positive integer represented by string, whose length will not exceed 18.
If there is a tie, return the smaller one as answer.
'''
class Solution(object):
    def nearestPalindromic(self, S):
        """
        :type n: str
        :rtype: str
        """
        K = len(S)
        candidates = [str(10**k + d) for k in (K-1, K) for d in (-1, 1)]
        prefix = S[:(K+1)/2]
        P = int(prefix)
        for start in map(str, (P-1, P, P+1)):
            candidates.append(start + (start[:-1] if K%2 else start)[::-1])
        
        def delta(x):
            return abs(int(S) - int(x))
        
        ans = None
        for cand in candidates:
            if cand != S and not cand.startswith('00'):
                if (ans is None or delta(cand) < delta(ans) or
                        delta(cand) == delta(ans) and int(cand) < int(ans)):
                    ans = cand
        return ans


s = Solution()
s.nearestPalindromic('123')