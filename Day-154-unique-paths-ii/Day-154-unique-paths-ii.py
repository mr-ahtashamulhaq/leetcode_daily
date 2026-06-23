class Solution:
    def memoization(self, i, j, grid, dp):
        if i < 0 or j < 0:
            return 0

        if grid[i][j] == 1:
            return 0

        if i == 0 and j == 0:
            return 1
        
        if dp[i][j] != -1:
            return dp[i][j]

        up = self.memoization(i - 1, j, grid, dp)
        left = self.memoization(i, j - 1, grid, dp)

        dp[i][j] = up + left
        return dp[i][j]

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        return self.memoization(m - 1, n - 1, obstacleGrid , dp)