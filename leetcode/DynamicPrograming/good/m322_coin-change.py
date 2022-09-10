'''
https://leetcode.com/problems/coin-change/description/

You are given coins of different denominations and a total amount of money amount. Write a function to compute the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:

Input: coins = [1, 2, 5], amount = 11
Output: 3 
Explanation: 11 = 5 + 5 + 1
Example 2:

Input: coins = [2], amount = 3
Output: -1
Note:
You may assume that you have an infinite number of each kind of coin.
'''

import sys
class Solution(object):
    # DP solution
    
    # int coinChange(vector<int>& coins, int amount) {
    #     int Max = amount + 1;
    #     vector<int> dp(amount + 1, Max);
    #     dp[0] = 0;
    #     for (int i = 1; i <= amount; i++) {
    #         for (int j = 0; j < coins.size(); j++) {
    #             if (coins[j] <= i) {
    #                 dp[i] = min(dp[i], dp[i - coins[j]] + 1);
    #             }
    #         }
    #     }
    #     return dp[amount] > amount ? -1 : dp[amount];
    # }

    def coinChange_dfs_wrong(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        """
        if amount <= 0 or len(coins) <= 0: return 0
        coins.sort(reverse=True)

        memo = {}
        def search(n, i, min_count):
            if (n, i) in memo: 
                return memo[(n, i)]
            if coins[i] <= 0: return -1

            if n < coins[i]:
                return search(n, i+1, min_count)
            
            div, mod = divmod(n, coins[i])
            if div >= min_count:
                return -1

            if i + 1 == len(coins) and mod > 0:
                memo[(n, i)] = -1
                return -1

            if mod == 0: 
                memo[(n, i)] = div
                return div

            for j in xrange(div):
                count = search(mod + j * coins[i], i+1, min_count)
                if count >= 0:
                    min_count = min(min_count, count + div - j)

            ans = min_count if min_count != sys.maxint else -1
            memo[(n, i)] = ans
            return ans

        ans = search(amount, 0, sys.maxint)
        # print memo
        return ans


s = Solution()
# assert s.coinChange([1,2,5], 11) == 3
# assert s.coinChange([1,2,5], 10000) == 2000
# assert s.coinChange([2], 3) == -1
# assert s.coinChange(range(0,1025,2), 1000) == 1
# assert s.coinChange([0,1,2,3], 1000000000) == 333333334
print s.coinChange([0,100,51,31,2], 123456) #== 1243