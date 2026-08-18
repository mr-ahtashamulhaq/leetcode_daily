class Solution:
    def memoization(self, index, dp, nums):
        if index == 0:
            return nums[index]

        if index < 0:
            return 0

        if dp[index] != -1:
            return dp[index]

        pick = nums[index] + self.memoization(index - 2, dp, nums)
        not_pick = 0 + self.memoization(index - 1, dp, nums)

        dp[index] = max(pick, not_pick)
        return dp[index]

        
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [-1 for _ in range(n + 1)]

        return self.memoization(n - 1, dp, nums)
        