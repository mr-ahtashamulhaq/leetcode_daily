class Solution(object):
    def minimumCost(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ans = nums[0]
        nums[1:] = sorted(nums[1:])
        ans += nums[1]
        ans += nums[2]
        return ans