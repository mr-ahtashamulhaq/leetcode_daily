class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i= 0
        n = len(nums)
        total = 0
        temp = 0
        while i<n:
            if nums[i] == 1:
                temp +=1
            else:
                total = max(temp , total)
                temp = 0
            i +=1
        return max(total,temp)
                