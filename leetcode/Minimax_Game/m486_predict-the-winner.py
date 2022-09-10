'''
https://leetcode.com/problems/predict-the-winner
https://leetcode.com/articles/predict-the-winner
Given an array of scores that are non-negative integers. Player 1 picks one of the numbers from either end of the array followed by the player 2 and then player 1 and so on. Each time a player picks a number, that number will not be available for the next player. This continues until all the scores have been chosen. The player with the maximum score wins. 

Given an array of scores, predict whether player 1 is the winner. You can assume each player plays to maximize his score. 

Example 1:

Input: [1, 5, 2]
Output: False
Explanation: Initially, player 1 can choose between 1 and 2. If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5. If player 2 chooses 5, then player 1 will be left with 1 (or 2). So, final score of player 1 is 1 + 2 = 3, and player 2 is 5. Hence, player 1 will never be the winner and you need to return False.



Example 2:

Input: [1, 5, 233, 7]
Output: True
Explanation: Player 1 first chooses 1. Then player 2 have to choose between 5 and 7. No matter which number player 2 choose, player 1 can choose 233.Finally, player 1 has more score (234) than player 2 (12), so you need to return True representing player1 can win.



Note:

1 <= length of the array <= 20. 
Any scores in the given array are non-negative integers and will not exceed 10,000,000.
If the scores of both players are equal, then player 1 is still the winner.

'''
class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        total = sum(nums)
        dp = {}
        score = self.predict(nums, 0, len(nums)-1, True, dp)
        return score >= total / float(2)
    
    def predict(self, nums, start, end, is_first, dp):
        if (start, end, is_first) in dp:
            return dp[(start, end, is_first)]
        if start > end:
            return 0
        if is_first:
            result = max(
                nums[start] + self.predict(nums, start+1, end, not is_first, dp),
                nums[end] + self.predict(nums, start, end-1, not is_first, dp)
            )
        else:
            result = min(
                self.predict(nums, start+1, end, not is_first, dp),
                self.predict(nums, start, end-1, not is_first, dp)
            )
        dp[(start, end, is_first)] = result
        return result

    def PredictTheWinner_slow(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        def pick(score, start, end, round):
            if start > end:
                return (round % 2) ^ (score[0] >= score[1])

            s1 = [0,0]
            s1[round % 2] = score[round % 2] + nums[start]
            s1[(round ^ 1) % 2] = score[(round ^ 1) % 2]
            if not pick(s1, start+1, end, round+1):
                return True

            s1[round % 2] = score[round % 2] + nums[end]
            s1[(round ^ 1) % 2] = score[(round ^ 1) % 2]
            if not pick(s1, start, end-1, round+1):
                return True

            return False

        return pick([0,0], 0, len(nums)-1, 0)

s = Solution()
print s.PredictTheWinner([1, 5, 233, 7,1, 5, 233, 7,1, 5, 233, 7,1, 5, 233, 7,1, 5, 233, 7]) == True
print s.PredictTheWinner([1, 5, 2]) == False
print s.PredictTheWinner([1]) == True
print s.PredictTheWinner([0]) == True
print s.PredictTheWinner([1,2]) == True
print s.PredictTheWinner([1,2,3,4]) == True

        