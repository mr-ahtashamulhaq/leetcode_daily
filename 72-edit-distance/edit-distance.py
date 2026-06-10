class Solution:
    def memoization(self, i, j, text1, text2, dp):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if dp[i][j] != -1:
            return dp[i][j]

        if text1[i] == text2[j]:
            dp[i][j] = self.memoization(i-1, j-1, text1, text2, dp)
        else:
            insert = 1 + self.memoization(i, j-1, text1, text2, dp)
            delete = 1 + self.memoization(i-1, j, text1, text2, dp)
            replace = 1 + self.memoization(i-1, j-1, text1, text2, dp)
            dp[i][j] = min(insert, delete, replace)

        return dp[i][j]

    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)
        dp = [[-1 for _ in range(n2)] for _ in range(n1)]
        return self.memoization(n1-1, n2-1, word1, word2, dp)