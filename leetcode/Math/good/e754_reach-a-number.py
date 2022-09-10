'''
https://leetcode.com/problems/reach-a-number
https://leetcode.com/articles/reach-a-number

You are standing at position 0 on an infinite number line.  There is a goal at position target.

On each move, you can either go left or right.  During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.


Example 1:

Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.



Example 2:

Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.



Note:
target will be a non-zero integer in the range [-10^9, 10^9].
'''
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        
        # very good explanation
        # https://leetcode.com/problems/reach-a-number/discuss/112968/Short-JAVA-Solution-with-Explanation

        # find the first step k that sum(1:k) = 1+2+3+...+k > target
        # we can switch ith step to left, then the sum will become sum(1:k) - 2*i
        # if the gap sum(1:k) - target = 2X, find some nums that their sum equal to X
        # otherwise increase k to k+1 or k+2 to make the gap to be even