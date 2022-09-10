'''
https://leetcode.com/problems/longest-palindromic-substring/description/

Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.
Example 2:

Input: "cbbd"
Output: "bb"

'''

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s)<2 or s==s[::-1]:
            return s
        
        n=len(s)
        start,max_len=0,1
        for i in range(1,n):
            print i, s[i], max_len
            odd=s[i-max_len-1:i+1]
            even=s[i-max_len:i+1]
            if i-max_len-1>=0 and odd==odd[::-1]:
                start=i-max_len-1
                max_len+=2
                continue
            if i-max_len>=0 and even==even[::-1]:
                start=i-max_len
                max_len+=1
            
        return s[start:start+max_len]

    def longestPalindrome_manacher(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        if not s: return ''

        maxLen, maxC = 0, 0
        # manachers
        A = '@#' + '#'.join(s) + '#$'
        P = [0] * len(A)

        center = right = 0

        for i in xrange(1,len(A) - 1):
            if i < right:
                P[i] = min(right-i, P[2*center - i])
            while A[i+P[i]+1] == A[i-P[i]-1]:
                P[i] += 1

            if i > right:
                center, right = i, i + P[i]

            if P[i] > maxLen:
                maxLen = P[i]
                maxC = i
        
        return A[maxC-P[maxC]:maxC+P[maxC]+1].replace('#','')


s = Solution()

# print s.longestPalindrome('') == ''
# print s.longestPalindrome('babad') == 'bab'
# print s.longestPalindrome('aba') == 'aba'
# print s.longestPalindrome('ab') == 'a'
# print s.longestPalindrome('aaaaaaaaaaaaaa') == 'aaaaaaaaaaaaaa'


def isPalindrome(s):
    for i in xrange(len(s)//2):
        if s[i] != s[-i-1]: return False
    else:
        return True

print 'a'*1000000

print isPalindrome(s)