class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        word= strs[0]
        LCP = ""
        n = len(strs)
        for i in range(len(word)):

            for second_word in strs[1:]:
                if len(second_word) <= i or word[i] != second_word[i]:
                    return LCP
            LCP += word[i]
        return LCP