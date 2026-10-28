class Solution:
    def memoization(self, row, col, triangle, dp):
        if row == len(triangle) - 1:
            return triangle[row][col]
        
        if dp[row][col] is not None:
            return dp[row][col]

        down = triangle[row][col] + self.memoization(row + 1, col, triangle, dp)
        diagonal = triangle[row][col] + self.memoization(row + 1, col + 1, triangle, dp)

        dp[row][col] = min(down, diagonal)
        return dp[row][col]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)
        dp = [[None] * n for i in range(1,n + 1)]

        return self.memoization(0, 0, triangle, dp)
