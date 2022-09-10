'''
https://leetcode.com/problems/palindrome-partitioning
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.

Example:


Input: "aab"
Output:
[
  ["aa","b"],
  ["a","a","b"]
]

'''

class Solution:
    # refer to http://www.jiuzhang.com/solutions/palindrome-partitioning/
    def isPalindrome(self, s):
        for i in range(len(s)):
            if s[i] != s[len(s)-1-i]: return False
        return True
    
    def dfs(self, s, stringlist):
        if len(s) == 0: Solution.res.append(stringlist)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.dfs(s[i:], stringlist+[s[:i]])
            
    def partition(self, s):
        Solution.res = []
        self.dfs(s, [])
        return Solution.res