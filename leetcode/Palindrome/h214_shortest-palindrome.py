'''
https://leetcode.com/problems/shortest-palindrome/description/

Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:

Input: "aacecaaa"
Output: "aaacecaaa"
Example 2:

Input: "abcd"
Output: "dcbabcd"
'''

class Solution(object):
    def shortestPalindrome_bruteforce(self, s):
        r = s[::-1]
        for i in range(len(s) + 1):
            if s.startswith(r[i:]):
                return r[:i] + s

    def shortestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        # KMP based solution https://leetcode.com/problems/shortest-palindrome/discuss/60141/C++-8-ms-KMP-based-O(n)-time-and-O(n)-memory-solution
        # generate new string l = str + '#' + reversed str, 
        # rum KMP algorithm, the jump index of l[-1] will point to the end of the palindrome start from beginning

        rev = s[::-1]
        l = s + '#' + rev
        p = [0] * len(l)
        for i in xrange(1, len(p)):
            j = p[i-1]
            while j > 0 and l[i] != l[j]:
                j = p[j-1]
            if l[i] == l[j]:
                j += 1
            p[i] = j

        return rev[:len(s) - p[-1]] + s


s = Solution()
inp = 'a'*10000+'b'; print s.shortestPalindrome(inp) == s.shortestPalindrome_bruteforce(inp)
inp = 'b' + 'a'*10000; print s.shortestPalindrome(inp) == s.shortestPalindrome_bruteforce(inp)
