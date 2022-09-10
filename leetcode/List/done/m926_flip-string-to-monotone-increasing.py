'''
https://leetcode.com/problems/flip-string-to-monotone-increasing
https://leetcode.com/articles/flip-string-to-monotone-increasing
A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

 


Example 1:


Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.



Example 2:


Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.



Example 3:


Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.


 

Note:


	1 <= S.length <= 20000
	S only consists of '0' and '1' characters.




'''
class Solution(object):
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        if not S: return 0
        
        leftone = [0] * len(S)
        rightzero = [0] * len(S)
        
        left = 0 if S[0] == '0' else 1
        for i in xrange(1, len(S)):
            leftone[i] = left
            left += 0 if S[i] == '0' else 1
        
        right = 0 if S[-1] == '1' else 1
        for i in range(len(S)-1)[::-1]:
            rightzero[i] = right
            right += 0 if S[i] == '1' else 1
        
        ans = len(S)
        for i in xrange(len(S)):
            ans = min(ans, leftone[i] + rightzero[i])
        return ans
        