# LeetCode 121 - Best Time to Buy and Sell Stock (Easy)
#
# Given an array prices where prices[i] is a stock's price on day i, pick one
# day to buy and a later day to sell so as to maximize your profit. Return that
# maximum profit, or 0 if no profitable trade exists.
#
# You must buy before you sell, so the answer is not simply max - min. Prices
# that only ever fall give 0, and a single day gives 0.
#
# Example: [7,1,5,3,6,4]  ->  5   (buy at 1, sell at 6)
#          [7,6,4,3,1]    ->  0
#
# Another solution to this same problem is in bestTimeToBuyandSellStock.py.

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # create our max profit of selling a stock and two pointer method which will create our window.
        maxP = 0
        i = 0
        j = 1
        # each iteration, if there is a lower baseline price, set i to that price. else continue moving right pointer calculating profit and looking for a lower low, and higher profit. 
        while j < len(prices):
            sum = prices[j] - prices[i]

            if prices[j] < prices[i]:
                i = j
                j += 1
            else:
                j += 1
                maxP = max(maxP, sum)

        return maxP