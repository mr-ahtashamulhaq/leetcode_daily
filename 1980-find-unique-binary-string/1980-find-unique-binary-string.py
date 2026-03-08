class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        one_word = "".join( ["1" * n] )
        nums = set(nums)

        for i in range(n):
            if one_word not in nums:
                return one_word
            else:
                one_word = "0" + one_word[:-1]

        return one_word