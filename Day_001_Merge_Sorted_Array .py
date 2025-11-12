# 88. Merge Sorted Array

"""You are given two integer array nums1 and nums2, sorted in increasing order, and two integers m and n, representing the number of elements in nums1 and nums2 respectively.

Merge nums1 and nums2 into a single array sorted in non-decreasing order.

The final sorted array should not be returned by the function, but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
"""

from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

        if m == 0:
            for i in range(n):
                nums1[i] = nums2[i]
        else:
            tail1 = m - 1
            tail2 = n - 1
            curr = (m + n) - 1
            while tail1 >= 0 and tail2 >= 0:

                if nums1[tail1] <= nums2[tail2]:
                    nums1[curr] = nums2[tail2]
                    tail2 -= 1

                elif nums1[tail1] > nums2[tail2]:
                    nums1[curr] = nums1[tail1]
                    tail1 -= 1

                curr -= 1

            if tail2 >= 0:
                for i in range(tail2, -1, -1):
                    nums1[i] = nums2[i]


sol = Solution()
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

sol.merge(nums1, m, nums2, n)
print(nums1)

# Output : [1, 2, 2, 3, 5, 6]