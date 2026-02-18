class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        word = strs[0]
        LCP = ""

        for i in range(len(word)):

            for second_word in strs:
                if i >= len(second_word) or word[i] != second_word[i]:
                    return LCP
                
            LCP += word[i]
        return LCP
