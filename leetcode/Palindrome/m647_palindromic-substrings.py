'''
https://leetcode.com/problems/palindromic-substrings/description/

Given a string, your task is to count how many palindromic substrings in this string.

The substrings with different start indexes or end indexes are counted as different substrings even they consist of same characters.

Example 1:
Input: "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:
Input: "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
Note:
The input string length won't exceed 1000.
'''

# 1. Bruce force: O(N^3) time
# 2. 

from collections import deque
class Solution(object):
    def countSubstrings_manachers(self, s):
        """
        :type s: str
        :rtype: int
        """
        def manachers(S):
            A = '@#' + '#'.join(S) + '#$'
            Z = [0] * len(A)
            center = right = 0
            for i in xrange(1, len(A) - 1):
                if i < right:
                    Z[i] = min(right - i, Z[2 * center - i])
                while A[i + Z[i] + 1] == A[i - Z[i] - 1]:
                    Z[i] += 1
                if i + Z[i] > right:
                    center, right = i, i + Z[i]
            return Z

        return sum((v+1)/2 for v in manachers(s))  

    def countSubstrings(self, s):
        # DP solution, dp[i] keep all palindromic substrings (k, i) ends at index i
        # for i+1, if k == i and s[i] == s[i+1], we found one (i, i+1)
        # other candidates, (k, i) we compare s[k-1] and s[i+1], if equal, we found another (k-1, i+1)
        # in implememtation, use deque to push/pop
        
        queue = deque()
        size = 0
        ans = 0
        for i, c in enumerate(s):
            cur, size = size, 0
            for j in xrange(cur):
                l, r = queue.popleft()
                if l == r and s[l] == c:
                    queue.append((l, i))
                    size += 1
                if l > 0 and s[l-1] == c:
                    queue.append((l-1, i))
                    size += 1

            queue.append((i, i))
            size += 1
            ans += size

        return ans

s = Solution()
print s.countSubstrings("") == 0
print s.countSubstrings("a") == 1
print s.countSubstrings("abc") == 3
print s.countSubstrings("aaa") == 6
print s.countSubstrings("aaaaaaaaaaabbbaaa") == 81
print s.countSubstrings("abcddcba") == 12
        