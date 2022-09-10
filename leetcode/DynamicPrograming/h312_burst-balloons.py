'''
https://leetcode.com/problems/burst-balloons/description/

Given n balloons, indexed from 0 to n-1. Each balloon is painted with a number on it represented by array nums. You are asked to burst all the balloons. If the you burst balloon i you will get nums[left] * nums[i] * nums[right] coins. Here left and right are adjacent indices of i. After the burst, the left and right then becomes adjacent.

Find the maximum coins you can collect by bursting the balloons wisely.

Note:

You may imagine nums[-1] = nums[n] = 1. They are not real therefore you can not burst them.
0 <= n <= 500, 0 <= nums[i] <= 100
Example:

Input: [3,1,5,8]
Output: 167 
Explanation: nums = [3,1,5,8] --> [3,5,8] -->   [3,8]   -->  [8]  --> []
             coins =  3*1*5      +  3*5*8    +  1*3*8      + 1*8*1   = 167
'''
import sys
class Solution(object):
    def maxCoins(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # credit to https://leetcode.com/problems/burst-balloons/discuss/76228
        memo = {}
        def burst(left, right):
            if left + 1 == right: return 0
            if (left, right) in memo:
                return memo[(left, right)]

            ans = 0
            for i in xrange(left+1, right):
                # burst left and right first, then burst ballon i
                ans = max(ans, nums[left] * nums[i] * nums[right] + burst(left, i) + burst(i, right))

            memo[(left, right)] = ans
            return ans

        nums = [1] + nums + [1]
        return burst(0, len(nums)-1)

    def maxCoins2(self, nums):
        # dp[i][j] means the max coin we get after burst ballons between i and j
        # dp[i][j] = max(dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j]), where i < k < j
        # dp[0][n-1] is the answer.
        nums = [1] + nums + [1]
        n = len(nums)
        dp = [[0] * n for _ in xrange(n)]

        # wrong implementation, the end state should be i + 2 = j, 
        # which means only one ballon with two boundaries.
        # refer to maxCoins_dp
        for j in xrange(2, n):  
            for i in xrange(j):
                print i, j
                for k in xrange(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k] + dp[k][j] + nums[i]*nums[k]*nums[j])
        print dp
        return dp[0][n-1]



    def maxCoins_dp(self, iNums):
        nums = [1] + [i for i in iNums if i > 0] + [1]
        n = len(nums)
        dp = [[0]*n for _ in xrange(n)]

        for k in xrange(2, n):
            for left in xrange(0, n - k):
                right = left + k
                print left, right
                for i in xrange(left + 1,right):
                    dp[left][right] = max(dp[left][right],
                           nums[left] * nums[i] * nums[right] + dp[left][i] + dp[i][right])
        print dp
        return dp[0][n - 1]



    # though it's in DP category, i'm still trying greedy
    # we pre-compute the coins, each iteration, we burst the ballon that can create max gain or minumum lose
    def maxCoins_wrong(self, nums):
        coins = [0]
        for i in xrange(len(nums)):
            left = nums[i-1] if i > 0 else 1
            right = nums[i+1] if i < len(nums)-1 else 1
            coins.append(left * nums[i] * right)
        coins.append(0)
        nums = [1] + nums + [1]

        ans = 0
        while len(coins) > 2:
            i, maxDelta = 0, - sys.maxint
            for j in xrange(1, len(coins)-1):
                delta = coins[j] + coins[j-1] / nums[j] * nums[j+1] + coins[j+1] / nums[j] * nums[j-1] - coins[j-1] - coins[j+1]
                if delta >= maxDelta:
                    maxDelta = delta
                    i = j

            ans += coins[i]
            coins[i-1] = coins[i-1] / nums[i] * nums[i+1]
            coins[i+1] = coins[i+1] / nums[i] * nums[i-1]

            coins = coins[:i] + coins[i+1:]
            nums = nums[:i] + nums[i+1:]

        return ans

s = Solution()
# print s.maxCoins([3,1,5,8]) == 167
# print s.maxCoins([3,1,5,8,10, 3,1,5,8,9]) == 2551
# print s.maxCoins(range(1,20)) == 36860

print s.maxCoins2([3,1,5,8]) == 167
print s.maxCoins_dp([3,1,5,8]) == 167
# print s.maxCoins2([3,1,5,8,10, 3,1,5,8,9]) == 2551
# print s.maxCoins2(range(1,20)) == 36860