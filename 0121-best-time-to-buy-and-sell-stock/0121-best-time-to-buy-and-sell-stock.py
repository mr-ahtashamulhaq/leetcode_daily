class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        mini = prices[0]
        maxProfit = 0
        
        for i in range(1, len(prices)):
            if ((prices[i] - mini ) > maxProfit ):
                maxProfit = max(prices[i]-mini , maxProfit)
            mini = min(mini, prices[i])
        return maxProfit

