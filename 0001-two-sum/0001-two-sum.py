class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}
        for i in  range(len(nums)):
            remaining = target - nums[i]
            if remaining in seen:
                return [i,seen[remaining]]
            else:
                seen[nums[i]] = i