'''
https://leetcode.com/problems/shortest-distance-to-a-character
https://leetcode.com/articles/shortest-distance-to-a-character
Given a string S and a character C, return an array of integers representing the shortest distance from the character C in the string.

Example 1:


Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]


 

Note:


	S string length is in [1, 10000].
	C is a single character, and guaranteed to be in string S.
	All letters in S and C are lowercase.

'''

class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        if not S: return []
        
        pos = []
        for i,c in enumerate(S):
            if c == C:
                pos.append(i)
        
        j = 0
        ans = []
        l, r = pos[j], pos[j+1] if j+1 < len(pos) else 2 * len(S)
        for i,c in enumerate(S):
            if i <= l:
                ans.append(l - i)
            else:
                ans.append(min(i-l, r-i))
            
            if i >= r:
                j += 1
                l, r = pos[j], pos[j+1] if j+1 < len(pos) else 2 * len(S)
        
                    
        return ans


s = Solution()

print s.shortestToChar("l", 'l') == [0]
print s.shortestToChar("", '') == []
print s.shortestToChar("loveleetcode", 'e') == [3,2,1,0,1,0,0,1,2,2,1,0]