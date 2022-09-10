'''
https://leetcode.com/problems/restore-ip-addresses/description/

Given a string containing only digits, restore it by returning all possible valid IP address combinations.

Example:

Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
'''

'''

ip v4 rules: a.b.c.d, for all 0<=a,b,c,d <= 255

greedy + backtracking

'''

class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
