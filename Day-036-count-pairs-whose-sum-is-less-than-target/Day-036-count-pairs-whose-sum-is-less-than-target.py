class Solution(object):
    def countPairs(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        count = 0
        n = len(nums)
        i = 0
        j = n-1
        nums.sort()
        while i < j:
            sumRes = nums[i] + nums[j]
            if sumRes < target:
                count += (j - i)
                i +=1
            else:
                j -= 1
        return count