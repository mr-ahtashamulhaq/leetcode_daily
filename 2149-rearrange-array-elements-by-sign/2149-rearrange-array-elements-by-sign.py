class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [0] * len(nums)
        posind= 0
        negind = 1
        for num in nums:
            if num>= 0:
                result[posind] = num
                posind +=2
            else:
                result [negind] = num
                negind +=2
        return result