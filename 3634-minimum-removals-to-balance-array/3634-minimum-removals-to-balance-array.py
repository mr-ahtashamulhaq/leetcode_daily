class Solution(object):
    def minRemoval(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        n = len(nums)
        nums.sort()
        
        min_removal = n - 1
        i, j = 0, 0
        
        while j < n:
            if nums[j] <= nums[i] * k:
                j += 1
            else:
                i += 1
            
            min_removal = min(min_removal, n - (j - i))
        
        return min_removal