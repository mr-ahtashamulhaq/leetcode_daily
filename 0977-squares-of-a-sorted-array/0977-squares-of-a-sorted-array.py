class Solution(object):
    def sortedSquares(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums) -1
        ind = len(nums ) - 1
        result= [0 for X in range(len(nums))]

        while i  <= j:
            if abs(nums[i]) > abs(nums[j]):
                result[ind] = nums[i]**2
                i +=1
            else:
                result[ind] = nums[j]**2
                j -=1
            ind -=1
        return result
