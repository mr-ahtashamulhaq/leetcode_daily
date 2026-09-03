class Solution:
    def frequencySort(self, s: str) -> str:
        freq = {}
        for ch in s:
            freq[ch] = freq.get(ch, 0) + 1
        sortedItem = sorted(freq.items(), key = lambda x:x[1] , reverse = True)

        result = ""
        for key, val in sortedItem:
            result += key * val

        return result