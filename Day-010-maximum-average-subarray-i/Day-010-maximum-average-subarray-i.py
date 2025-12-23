class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        if len(nums) == 1:
            return nums[0]
        maxi = 0.0
        for i in range(k):
            maxi += nums[i]
        

        i = 0
        j = k
        maxi = maxi/k
        while i <n and j< n:
            maxi = max(maxi, ((maxi-nums[i] )+ nums[j])/k)
            i +=1
            j+=1
        return maxi