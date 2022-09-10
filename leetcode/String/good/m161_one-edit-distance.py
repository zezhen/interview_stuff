'''
https://leetcode.com/problems/one-edit-distance

Given two strings s and t, determine if they are both one edit distance apart.

Note: 

There are 3 possiblities to satisify one edit distance apart:

Insert a character into s to get t
Delete a character from s to get t
Replace a character of s to get t
Example 1:

Input: s = "ab", t = "acb"
Output: true
Explanation: We can insert 'c' into s to get t.
Example 2:

Input: s = "cab", t = "ad"
Output: false
Explanation: We cannot get t from s by only one step.
Example 3:

Input: s = "1203", t = "1213"
Output: true
Explanation: We can replace '0' with '1' to get t.
'''

class Solution(object):
    def isOneEditDistance(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        # Anjian Sun said the best solution for a question is that can only solve this problem.

        # because only one edit distance, so use two point to scan both strings
        # while we need to know which string is longer
        ls, lt = len(s), len(t)
        if abs(ls - lt) > 1: return False

        if ls > lt:
        	longer  = s
        	shorter = t
        else:
        	longer  = t
        	shorter = s

        i, j, mismatch = 0, 0, 0
        while i < ls and j < lt:
        	if s[i] == t[j]:
        		i += 1
        		j += 1
        		continue

        	i += 1
        	if ls == lt:
        		j += 1
        	mismatch += 1
        	if mismatch > 1: return False

        return True

s = Solution()
assert s.isOneEditDistance(s = "ab", t = "acb") == True
assert s.isOneEditDistance(s = "cab", t = "ad") == False
assert s.isOneEditDistance(s = "1203", t = "1213") == True
