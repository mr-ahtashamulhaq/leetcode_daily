class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        # s = list(s)
        # t = list(t)

        i , j = 0, 0
        res_s = []
        for i in range(len(s)):
            if res_s ==[] and s[i] == "#" :
                continue
            elif s[i] == "#":
                res_s.pop()
            else:
                res_s.append(s[i])

                
        res_t = []
        for i in range(len(t)):
            if res_t == [] and t[i] == "#":
                continue
            elif t[i] == "#":
                res_t.pop()
            else:
                res_t.append(t[i])
        
        return res_s == res_t
        