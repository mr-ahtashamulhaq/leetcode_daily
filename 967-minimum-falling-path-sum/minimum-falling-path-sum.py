class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]):
        n = len(matrix)
        dp = [[None for _ in range(n)] for _ in range(n)]

        for j in range(n):
            dp[0][j] = matrix[0][j]

        for i in range(1, n):
            for j in range(0, n):
       
                up = matrix[i][j] + dp[i - 1][j]
                if j == 0:
                    left = float("inf")
                else:
                    left = matrix[i][j] + dp[i - 1][j - 1]

  
                if j == n - 1:
                    right = float("inf")
                else:
                    right = matrix[i][j] + dp[i - 1][j + 1]
         
                dp[i][j] = min(left, up, right)
     
        mini = float("inf")
        for j in range(n):
            mini = min(mini, dp[n - 1][j])
        return mini