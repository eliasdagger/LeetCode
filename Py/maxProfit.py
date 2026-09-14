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