class Solution:
    def firstUniqueEven(self, nums: list[int]) -> int:
        freq = {}
        for i in nums:
            if i%2 == 0:
                freq[i] = freq.get(i, 0) + 1

        for key,val in freq.items():
            if freq[key] == 1:
                return key
        return -1