'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee

Your are given an array of integers prices, for which the i-th element is the price of a given stock on day i; and a non-negative integer fee representing a transaction fee.
You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.  You may not buy more than 1 share of a stock at a time (ie. you must sell the stock share before you buy again.)
Return the maximum profit you can make.

Example 1:

Input: prices = [1, 3, 2, 8, 4, 9], fee = 2
Output: 8
Explanation: The maximum profit can be achieved by:
Buying at prices[0] = 1Selling at prices[3] = 8Buying at prices[4] = 4Selling at prices[5] = 9The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.



Note:
0 < prices.length <= 50000.
0 < prices[i] < 50000.
0 <= fee < 50000.
'''
class Solution(object):
    def maxProfit(self, prices, fee):
        """
        :type prices: List[int]
        :type fee: int
        :rtype: int
        """
        # follow the idea from best-time-to-buy-and-sell-stock-with-cooldown
        # construct the transaction sequence
        # buy[i] = max(buy[i-1], sell[i] - price[i])
        # sell[i] = max(sell[i-1], buy[i-1] + price[i] - fee)
        # change to O(1) space solution

        if len(prices) < 2: return 0

        buy, sell, prev_buy, prev_sell = 0, 0, -prices[0], 0
        for i in xrange(1, len(prices)):
            buy = max(prev_buy, prev_sell - prices[i])
            prev_buy = buy
            sell = max(prev_sell, prev_buy + prices[i] - fee)
            prev_sell = sell

        return sell

s = Solution()
print s.maxProfit([1, 3, 2, 8, 4, 9], 2) == 8
print s.maxProfit([1, 3, 2, 8, 4, 9], 3) == 6
            