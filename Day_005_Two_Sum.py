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