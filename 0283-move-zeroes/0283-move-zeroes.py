class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) == 1:
            return
        i = 0
        j = 0

        while i < len(nums) and j < len(nums):
            while i < len(nums) and nums[i] != 0:
                i+=1
            j = i+1 
            while j < len(nums) and nums[j] == 0:
                j+=1
            if j < len(nums):
                nums[i],nums[j]=nums[j],nums[i]
            i+=1
            # j+=1

        