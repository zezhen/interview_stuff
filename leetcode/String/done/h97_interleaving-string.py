'''
https://leetcode.com/problems/interleaving-string/description/

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
'''

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """
        if len(s1) + len(s2) != len(s3):
            return False
        if (s1 == s2 == s3 == "") or \
            (s1 == "" and s2 == s3) or \
            (s2 == "" and s1 == s3):
            return True
        
        # use cache to keep the result memory of index pair (i1, i2)
        self.cache = {}
        self.cache[(len(s1), len(s2))] = True
        
        i1 = i2 = 0
        return self._isInterleave(s1, s2, s3, 0, 0)
    
    def _isInterleave(self, s1, s2, s3, i1, i2):
        if (i1, i2) in self.cache:
            return self.cache[(i1, i2)]
        
        ans = False
        
        if i1 < len(s1) and (i1+i2) < len(s3) and s1[i1] == s3[i1 + i2]:
            ans |= self._isInterleave(s1, s2, s3, i1 + 1, i2)
            self.cache[(i1 + 1, i2)] = ans
            if ans:
                return ans
        
        if i2 < len(s2) and (i1+i2) < len(s3) and s2[i2] == s3[i1 + i2]:
            ans |= self._isInterleave(s1, s2, s3, i1, i2 + 1)
            self.cache[(i1, i2 + 1)] = ans
            
        return ans