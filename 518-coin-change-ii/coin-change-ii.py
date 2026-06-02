class Solution:
    def memoization(self, index, amount, coins, dp):
        if index == 0:
            if amount % coins[0] == 0:
                return 1
            return 0

        if dp[index][amount] != -1:
            return dp[index][amount]

        not_pick = self.memoization(index - 1, amount, coins, dp)

        # pick current coin (only if coin <= amount)
        pick = 0
        if coins[index] <= amount:
            pick = self.memoization(index, amount - coins[index], coins, dp)

        dp[index][amount] = pick + not_pick
        return dp[index][amount]

    def change(self, amount: int, coins) -> int:

        n = len(coins)
        dp = [[-1 for _ in range(amount + 1)] for _ in range(n)]
        return self.memoization(n - 1, amount, coins, dp)