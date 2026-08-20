class Solution:
    def romanToInt(self, s: str) -> int:
        hashmap = {"I" : 1,
                    "V" : 5,
                    "X" : 10,
                    "L" : 50,
                    "C" : 100,
                    "D" : 500,
                    "M" : 1000}
        n = len(s)
        i = 0
        result = 0
        while i < n:
            if i < n-1 and hashmap[s[i]] < hashmap[s[i+1]]:
                val = hashmap[s[i+1]] - hashmap[s[i]]
                result += val
                i +=2
            else:
                result += hashmap[s[i]]
                i +=1
        
        return result
                