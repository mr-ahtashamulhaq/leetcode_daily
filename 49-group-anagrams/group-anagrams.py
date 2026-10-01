class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {}
        result = []
        
        for string in strs:
            sorted_word = ''.join(sorted(string))
            if sorted_word not in dictionary:
                dictionary[sorted_word] = []
            dictionary[sorted_word].append(string)
        result = list(dictionary.values())
        return result