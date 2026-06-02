class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None
        """
        def reverse(nums, l, r):
            while l < r:
                nums[l], nums[r] = nums[r], nums[l]
                r -= 1
                l += 1

        n = len(nums)
        k %= n  
        reverse(nums, n - k, n - 1)
        reverse(nums, 0, n - k - 1)
        reverse(nums, 0, n - 1)