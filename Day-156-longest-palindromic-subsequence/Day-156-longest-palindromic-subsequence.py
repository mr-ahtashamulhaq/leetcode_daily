class Solution:
    #USING TABULATION
    def longestPalindromeSubseq(self, s):
        text1 = s
        text2 = s[::-1]
        n = len(s)
        dp = [[-1 for _ in range(n+1)] for _ in range(n+1)]

        for ind1 in range(n + 1):
            dp[ind1][0] = 0
        for ind2 in range(n + 1):
            dp[0][ind2] = 0

        for ind1 in range(1, n + 1):
            for ind2 in range(1, n + 1):
                if text1[ind1 - 1] == text2[ind2 - 1]:
                    dp[ind1][ind2] = 1 + dp[ind1 - 1][ind2 - 1]
                else:
                    dp[ind1][ind2] = 0 + max(dp[ind1 - 1][ind2], dp[ind1][ind2 - 1])

        return dp[n][n]