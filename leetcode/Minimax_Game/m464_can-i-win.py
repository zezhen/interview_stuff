'''
https://leetcode.com/problems/can-i-win/description/

In the "100 game," two players take turns adding, to a running total, any integer from 1..10. The player who first causes the running total to reach or exceed 100 wins.

What if we change the game so that players cannot re-use integers?

For example, two players might take turns drawing from a common pool of numbers of 1..15 without replacement until they reach a total >= 100.

Given an integer maxChoosableInteger and another integer desiredTotal, determine if the first player to move can force a win, assuming both players play optimally.

You can always assume that maxChoosableInteger will not be larger than 20 and desiredTotal will not be larger than 300.

Example

Input:
maxChoosableInteger = 10
desiredTotal = 11

Output:
false

Explanation:
No matter which integer the first player choose, the first player will lose.
The first player can choose an integer from 1 up to 10.
If the first player choose 1, the second player can only choose integers from 2 up to 10.
The second player will win by choosing 10 and get a total = 11, which is >= desiredTotal.
Same with other integers chosen by the first player, the second player will always win.

'''

class Solution(object):
    memo = {}
    def canIWin(self, maxChoosableInteger, desiredTotal):
        """
        :type maxChoosableInteger: int
        :type desiredTotal: int
        :rtype: bool
        """
        memo = self.memo
        def canWin(candidates, target):
            if sum(candidates) < target: return False
            if candidates[-1] >= target: return True

            if (candidates, target) in memo:
                return memo[(candidates, target)]

            for i in xrange(len(candidates)):
                value = candidates[i]
                if not canWin(candidates[:i]+candidates[i+1:], target - value):
                    memo[(candidates, target)] = True
                    return True
            memo[(candidates, target)] = False
            return False

        return canWin(tuple(range(1, maxChoosableInteger+1)), desiredTotal)

s = Solution()
print s.canIWin(10, 11) == False
print s.canIWin(12, 11) == True
print s.canIWin(20, 300) == False
# print s.canIWin(20, 150) == False
print s.canIWin(5, 50) == False
