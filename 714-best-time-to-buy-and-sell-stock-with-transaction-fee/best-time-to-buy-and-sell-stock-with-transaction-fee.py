class Solution:
    def maxProfit(self, prices, fee) -> int:
        n = len(prices)

        ahead = [-1, -1]

        ahead[0] = 0
        ahead[1] = 0

        for index in range(n - 1, -1, -1):
            curr = [0, 0]
            for buy_choice in range(0, 2):
                if buy_choice == 1:
                    buy = -prices[index] + ahead[0]
                    not_buy = 0 + ahead[1]
                    profit = max(buy, not_buy)

                else:  # cannot buy but have choice to sel or not
                    sell = prices[index] - fee + ahead[1]
                    not_sell = 0 + ahead[0]
                    profit = max(sell, not_sell)

                curr[buy_choice] = profit
            ahead = curr.copy()

        return ahead[1]
