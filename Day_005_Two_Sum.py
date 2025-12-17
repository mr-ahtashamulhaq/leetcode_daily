from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        seen = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            seen[nums[i]] = i


