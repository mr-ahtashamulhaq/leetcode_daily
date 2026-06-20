class Solution:
    def singleNumber(self, nums: List[int]) -> int:

        ans = 0

        # if we xor two same numbers it would return 0 and if we xor any number with 0 it would return that number

        for i in nums:
            ans = ans ^ i
        return ans
        