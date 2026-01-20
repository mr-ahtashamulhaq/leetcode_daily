class Solution:
    def memoization(self, index, buy_choice, prices, dp):
        n = len(prices)
        if index >= n:
            return 0

        if dp[index][buy_choice] != -1:
            return dp[index][buy_choice]

        if buy_choice == 1:
            not_buy = 0 + self.memoization(index + 1, 2, prices, dp)
            profit = not_buy

        elif buy_choice == 2:  # mean it can buy
            buy = -prices[index] + self.memoization(index + 1, 0, prices, dp)
            not_buy = 0 + self.memoization(index + 1, 2, prices, dp)
            profit = max(buy, not_buy)

        else:  # cannot buy but have choice to sel or not
            sell = prices[index] + self.memoization(index + 1, 1, prices, dp)
            not_sell = 0 + self.memoization(index + 1, 0, prices, dp)
            profit = max(sell, not_sell)

        dp[index][buy_choice] = profit
        return dp[index][buy_choice]

    def maxProfit(self, prices):
        n = len(prices)

        # DP will store dp[index][buy_choice] --> at this index with this buy value what would be highest profit
        dp = [[-1, -1, -1] for _ in range(n)]  # [-1, -1] --> [buy=0 , buy=1]
        return self.memoization(0, 2, prices, dp)
        