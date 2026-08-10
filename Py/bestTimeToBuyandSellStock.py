# LeetCode 121 - Best Time to Buy and Sell Stock (Easy)
#
# You are given an array prices where prices[i] is the price of a stock on day i.
# Pick one day to buy and a later day to sell, and return the largest profit you
# can make from that single transaction.
#
# You must buy before you sell. If no pair of days produces a profit, return 0.
#
# Example: prices = [7,1,5,3,6,4]  ->  5 (buy at 1 on day 2, sell at 6 on day 5)
#          prices = [7,6,4,3,1]    ->  0 (prices only fall, so don't trade)


def maxProfit(prices):
    maxP = 0
    i = 0
    j = 1
    while j < len(prices):
        sum = prices[j] - prices[i]

        if prices[j] < prices[i]:
            i = j
            j += 1
        else:
            j += 1
            maxP = max(maxP, sum)

    return maxP

print(maxProfit([7,1,5,3,6,4]))
        