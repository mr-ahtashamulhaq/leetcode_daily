# USING MEMOIZATION
class Solution:
    def memoization(self, index, remaining, arr, dp):
        if remaining == 0:
            return True
        if index == 0:
            return arr[0] == remaining

        if dp[index][remaining] != -1:
            return dp[index][remaining]

        ans1 = False
        if arr[index] <= remaining:
            ans1 = self.memoization(index - 1, remaining - arr[index], arr, dp)

        ans2 = self.memoization(index - 1, remaining, arr, dp)

        dp[index][remaining] = ans1 or ans2
        return dp[index][remaining]

    def canPartition(self, arr) -> bool:
        n = len(arr)
        total_sum = sum(arr)

        if total_sum % 2 != 0:
            return False

        target = total_sum // 2
        dp = [[-1 for _ in range(target + 1)] for _ in range(n)]

        return self.memoization(n - 1, target, arr, dp)