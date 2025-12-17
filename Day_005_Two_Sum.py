"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
"""
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int):
        seen = {}

        for i in range(len(nums)):
            remaining = target - nums[i]
            if remaining in seen:
                return [i, seen[remaining]]
            seen[nums[i]] = i


obj = Solution()
nums = [2, 7, 11, 15]
target = 9
print(obj.twoSum(nums, target))

# Output: [1, 0]