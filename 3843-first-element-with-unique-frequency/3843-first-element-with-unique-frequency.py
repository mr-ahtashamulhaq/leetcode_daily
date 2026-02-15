class Solution(object):
    def firstUniqueFreq(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 1:
            return nums[0]
        freq = {}
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i], 0) + 1

        freq_count = {}
        for i in freq.values():
            freq_count[i] = freq_count.get(i, 0) +1

        for i in nums:
            if freq_count[freq[i]] == 1:
                return i
        return -1
            