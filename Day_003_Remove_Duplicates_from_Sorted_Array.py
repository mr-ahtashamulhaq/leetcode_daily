# 26. Remove Duplicates from Sorted Array
"""Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same.

Consider the number of unique elements in nums to be k. After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. The remaining elements beyond index k - 1 can be ignored.
"""

from typing import List
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        j = 1

        while j < n:
            if nums[i] != nums[j]:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
            else:
                j += 1

        return i + 1


obj = Solution()
nums = [0, 1, 2, 2, 3, 0, 4, 2]
obj.removeDuplicates(nums)
print(nums)

# Output : [0, 1, 2, 3, 4, _, _, _]