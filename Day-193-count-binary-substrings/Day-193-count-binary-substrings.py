class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        curr = 1    #Will Track current streak
        prev = 0    #will track previous streak
        result = 0
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                curr +=1

            else:
                result += min(curr,prev)
                prev = curr
                curr = 1
                
        result += min(curr,prev)
        return result