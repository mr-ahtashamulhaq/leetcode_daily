class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        i = len(s) - 1

        temp = []
        result = ""

        while i != -1:
            if s[i] != " ":
                temp.append(s[i])
                i -= 1
            elif s[i] == " ":
                i -= 1
                while s[i] == " ":
                    i -=1              

                while temp != []:
                    result = result + temp.pop()
                result = result + " "
        while temp != []:
            result = result + temp.pop()
        return result