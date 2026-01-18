class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        n = len(nums)
        total_sum = sum(nums)
        dp = [[None for _ in range(2*total_sum + 1)] for _ in range(n)]

        return self.memoization(n - 1, 0, target, nums, dp)

    def memoization(self, index, summ, target, nums, dp):
        if index == 0:
            ways = 0
            if summ - nums[0] == target:
                ways += 1
            if summ + nums[0] == target:
                ways += 1
            return ways

        if dp[index][summ] is not None:
            return dp[index][summ]

        add = self.memoization(index - 1, summ + nums[index], target, nums, dp)

        subtract = self.memoization(index - 1, summ - nums[index], target, nums, dp)

        dp[index][summ] = add + subtract
        return dp[index][summ]     