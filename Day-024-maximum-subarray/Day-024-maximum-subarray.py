class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        current_sum = 0
        best_sum = float('-inf')
        
        for num in nums:
            current_sum += num
            best_sum = max(best_sum , current_sum)
            if current_sum < 0:
                current_sum = 0

        return best_sum
        