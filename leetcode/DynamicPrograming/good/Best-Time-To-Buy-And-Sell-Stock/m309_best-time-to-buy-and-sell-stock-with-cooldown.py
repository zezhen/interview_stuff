'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/description/

Say you have an array for which the ith element is the price of a given stock on day i.

Design an algorithm to find the maximum profit. You may complete as many transactions as you like (ie, buy one and sell one share of the stock multiple times) with the following restrictions:

You may not engage in multiple transactions at the same time (ie, you must sell the stock before you buy again).
After you sell your stock, you cannot buy stock on next day. (ie, cooldown 1 day)
Example:

Input: [1,2,3,0,2]
Output: 3 
Explanation: transactions = [buy, sell, cooldown, buy, sell]

'''

import sys
class Solution(object):
    # refer to https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/discuss/75927

    # first, construct transaction sequences 
    # buy[i]  = max(rest[i-1]-price, buy[i-1]) 
    # sell[i] = max(buy[i-1]+price, sell[i-1])
    # rest[i] = max(sell[i-1], buy[i-1], rest[i-1])
    # 
    # then, add constraints
    # buy[i] = max(sell[i-2]-price, buy[i-1])
    # sell[i] = max(buy[i-1]+price, sell[i-1])
    
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        for price in prices:
            prev_buy = buy
            buy = max(prev_sell - price, prev_buy)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell


    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if not prices or len(prices) <= 0:
            return 0
        # [[(bought_price, profit)]], 0->buy, 1->sell, 2->cooldown
        cache = []
        
        previous = [(-prices[0], 0), ('x', 0), ('x', 0)]
        for i in range(1, len(prices)):
            
            item = []
            pbuy = previous[0]
            psell = previous[1]
            pcooldown = previous[2]
            
            # buy <- previous cooldown
            item.append( (max(-prices[i], pbuy[0]), pcooldown[1]) )
            
            # sell <- previous buy or cooldown
            bprofit = (prices[i] + pbuy[0] if pbuy[0] <= 0 and prices[i] + pbuy[0] > 0 else 0) + pbuy[1]
            cprofit = (prices[i] + pcooldown[0] if pcooldown[0] <= 0 and prices[i] + pcooldown[0] > 0 else 0) + pcooldown[1]
            item.append( max([('x', max(bprofit, cprofit)), psell], key=lambda t:t[1]) )
            
            # cooldown <- buy, sell, cooldown
            item.append( max(previous, key=lambda t: (t[1], - sys.maxint if t[0] == 'x' else t[0])) )
            
            previous = item
            print previous
            
        return max(previous, key=lambda t:t[1])[1]

s = Solution()
print s.maxProfit([1,2,3,0,2]) == 3
print s.maxProfit([1,2,3,4,5]) == 4
