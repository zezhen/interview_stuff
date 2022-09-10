'''
https://leetcode.com/problems/paint-fence

There is a fence with n posts, each post can be painted with one of the k colors.

You have to paint all the posts such that no more than two adjacent fence posts have the same color.

Return the total number of ways you can paint the fence.

Note:
n and k are non-negative integers.

Example:

Input: n = 3, k = 2
Output: 6
Explanation: Take c1 as color 1, c2 as color 2. All possible ways are:

            post1  post2  post3      
 -----      -----  -----  -----       
   1         c1     c1     c2 
   2         c1     c2     c1 
   3         c1     c2     c2 
   4         c2     c1     c1  
   5         c2     c1     c2
   6         c2     c2     c1
'''
class Solution(object):
    def numWays(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # similar to numWays1 solution, but no more that two "adjacent fence posts have the same color"
        # will mark "c1 c1 c1" as invalid

        # dp[1] = (0, k)
        # dp[i] = (dp[i-1][1], dp[i-1][0] * (k-1) + dp[i-1][1] * (k-1))
        if n == 0 or k == 0: return 0

        has_dup, no_dup = 0, k
        while n > 1:
            has_dup, no_dup = no_dup, (no_dup + has_dup) * (k-1)
            n -= 1
        return no_dup + has_dup

    def numWays1(self, n, k):
        # mis-understad of "no more than two adjacent fence posts have the same color", 
        # i thought there is no more that two "adjacent fence posts have the same color"
        # base on that "c1 c1 c2 c2" will be invalid in my solution.

        # dp[i] = (has_dup, no_dup) by pos i, how many ways exist that has dup and no dup
        # dp[1] = (0, k)
        # dp[i] = (dp[i-1][0] * (k-1) + dp[i-1][1], dp[i-1][1] * (k-1))

        if n == 0 or k == 0: return 0
        has_dup, no_dup = 0, k
        while n > 1:
            has_dup, no_dup = has_dup * (k-1) + no_dup, no_dup * (k-1)
            n -= 1
            # print no_dup, has_dup
        return no_dup + has_dup


s = Solution()
assert s.numWays(0,2) == 0
assert s.numWays(3,0) == 0
assert s.numWays(3,1) == 0
assert s.numWays(1,3) == 3
assert s.numWays(3,2) == 6
assert s.numWays(4,2) == 10
assert s.numWays(3,3) == 24
assert s.numWays(4,3) == 66
assert s.numWays(5,3) == 180
assert s.numWays(10,5) == 7348480
