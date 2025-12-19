class Solution(object):
    def maxProfit(self, prices):

        minPrice = float("inf")
        maxProfit = 0
        
        for i in range( len(prices)):
            maxProfit = max(prices[i]-minPrice , maxProfit)
            minPrice = min(minPrice, prices[i])
        return maxProfit