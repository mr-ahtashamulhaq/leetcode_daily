class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        """
        n = len(nums)
        maxi = 0.0
        for i in range(k):
            maxi += nums[i]
        
        i = 0
        j = k
        currsum = maxi
        while i <n and j< n:
            currsum -= nums[i]
            i+=1
            currsum += nums[j]
            j+=1

            maxi = max(maxi, currsum)

        return maxi/k