'''
https://leetcode.com/problems/is-subsequence/description/

Given a string s and a string t, check if s is subsequence of t.

You may assume that there is only lower case English letters in both s and t. t is potentially a very long (length ~= 500,000) string, and s is a short string (<=100).

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (ie, "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
s = "abc", t = "ahbgdc"

Return true.

Example 2:
s = "axc", t = "ahbgdc"

Return false.

Follow up:
If there are lots of incoming S, say S1, S2, ... , Sk where k >= 1B, and you want to check one by one to see if T has its subsequence. In this scenario, how would you change your code?

'''

class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
'''
As subsequence need to keep the order, so scan both s and t, if s[i] == t[j], then j += 1, i += 1, else j += 1, until reach s or t's end

follow up:
1. create a trie tree from incoming S
2. maintain a next nodes list, scan t from head to tail, if check whether t[j] in nodes list, if yes, add the matching children node to list, j+=1

we can maintain a inverted map from char to nodes, so we don't need to scan whole nodes list 
'''