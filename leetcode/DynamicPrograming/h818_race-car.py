'''
https://leetcode.com/problems/race-car
https://leetcode.com/articles/race-car
Your car starts at position 0 and speed +1 on an infinite number line.  (Your car can go into negative positions.)

Your car drives automatically according to a sequence of instructions A (accelerate) and R (reverse).

When you get an instruction "A", your car does the following: position += speed, speed *= 2.

When you get an instruction "R", your car does the following: if your speed is positive then speed = -1 , otherwise speed = 1.  (Your position stays the same.)

For example, after commands "AAR", your car goes to positions 0->1->3->3, and your speed goes to 1->2->4->-1.

Now for some target position, say the length of the shortest sequence of instructions to get there.


Example 1:
Input: 
target = 3
Output: 2
Explanation: 
The shortest instruction sequence is "AA".
Your position goes from 0->1->3.



Example 2:
Input: 
target = 6
Output: 5
Explanation: 
The shortest instruction sequence is "AAARA".
Your position goes from 0->1->3->7->7->6.


 

Note: 


	1 <= target <= 10000.

'''
import sys
class Solution(object):
    def racecar(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        dp = [0] * (target + 1)

        for i in xrange(1, target + 1):
            dp[i] = sys.maxint
            j = m = 1
            while j < i:
                b = l = 0
                while l < j:
                    dp[i] = min(dp[i], m + 1 + b + 1 + dp[i - (j - l)])
                    b += 1
                    l = (1 << b) - 1
                m += 1
                j = (1 << m) - 1

            if i == j:
                dp[i] = min(dp[i], m)
            else:
                dp[i] = min(dp[i], m + 1 + dp[j - i])

        return dp[target]

s = Solution()
print s.racecar(3) == 2
print s.racecar(6) == 5
print s.racecar(10000) == 45


