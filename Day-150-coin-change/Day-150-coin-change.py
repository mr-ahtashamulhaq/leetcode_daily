class Solution:
    def recursion(self, index, amount, coins,dp):

        if index == 0:
            if amount % coins[index] == 0:
                return amount // coins[index]
            
            return float("inf")

        if dp[index][amount] != -1:
            return dp[index][amount]

        if coins[index] > amount:
            same_pick = float("inf")
        else:
            same_pick = 1 + self.recursion(index, amount - coins[index], coins,dp)

        prev_pick = 0 + self.recursion(index - 1, amount, coins,dp)

        dp[index][amount] = min(same_pick, prev_pick)
        return dp[index][amount]

    def coinChange(self, coins, amount):

        n = len(coins)
        dp= [[-1 for _ in range(amount+1)] for _ in range(n)]
        solve = self.recursion(n - 1, amount, coins,dp)
        if solve != float("inf"):
            return solve
        return -1