class Solution:
    def memoization(self, i, j, grid, dp):
        if i == 0 and j == 0:
            return grid[i][j]

        if i < 0 or j < 0:
            return float("inf")
        
        if dp[i][j] != -1:
            return dp[i][j]

        up = self.memoization(i - 1, j, grid, dp)
        left = self.memoization(i, j - 1, grid, dp)

        dp[i][j] = grid[i][j] + min(up, left)
        return dp[i][j]


    def minPathSum(self,grid):
        m = len(grid)
        n = len(grid[0])
        dp= [[-1 for _ in range(n)] for _ in range(m)]
        return self.memoization(m - 1, n - 1 , grid, dp)