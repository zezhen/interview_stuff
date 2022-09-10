'''
https://leetcode.com/problems/flip-game-ii

You are playing the following Flip Game with your friend: Given a string that contains only these two characters: + and -, you and your friend take turns to flip two consecutive "++" into "--". The game ends when a person can no longer make a move and therefore the other person will be the winner.

Write a function to determine if the starting player can guarantee a win.

Example:

Input: s = "++++"
Output: true 
Explanation: The starting player can guarantee a win by flipping the middle "++" to become "+--+".
Follow up:
Derive your algorithm's runtime complexity.
'''

class Solution(object):
    def canWin(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # wrong answer

        
        cache = {}
        def minFlip(n):
            if n <= 1: return 0
            if n <= 4: return 1
            if n in cache: return cache[n]

            i = n // 2
            flips = minFlip(i-1) + minFlip(n-i-1) + 1
            cache[n] = flips
            return flips

        res = minFlip(len(s)) % 2 == 1
        return res

s = Solution()

for i in xrange(1,20):
    print i, s.canWin('+'*i)

