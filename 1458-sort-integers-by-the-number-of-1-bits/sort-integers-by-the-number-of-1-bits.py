class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        result = sorted(arr, key = lambda x: ( x.bit_count(), x))
        return result