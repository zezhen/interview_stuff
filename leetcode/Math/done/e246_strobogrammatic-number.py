'''
https://leetcode.com/problems/strobogrammatic-number

A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic. The number is represented as a string.

Example 1:

Input:  "69"
Output: true
Example 2:

Input:  "88"
Output: true
Example 3:

Input:  "962"
Output: false
'''

class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        """
        if not num: return True

        _dict = {'6':'9','9':'6','0':'0','8':'8','1':'1'}
        n = len(num)
        for i in xrange(len(num) // 2 + 1):
            if _dict.get(num[i]) != num[-i-1]: return False

        return True

s = Solution()
print s.isStrobogrammatic("") == True
print s.isStrobogrammatic("6") == False
print s.isStrobogrammatic("0") == True
print s.isStrobogrammatic("8") == True
print s.isStrobogrammatic("619") == True
print s.isStrobogrammatic("649") == False
print s.isStrobogrammatic("8698") == True