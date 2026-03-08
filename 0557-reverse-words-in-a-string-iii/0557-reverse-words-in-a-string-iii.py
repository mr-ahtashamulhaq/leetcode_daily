class Solution:
    def reverseWords(self, s: str) -> str:
        words= s.split()
        result = ""
        size = len(words)
        for i, word in enumerate(words):
            result += word[::-1]
            if i != size-1:
                result += " "

            


        return result