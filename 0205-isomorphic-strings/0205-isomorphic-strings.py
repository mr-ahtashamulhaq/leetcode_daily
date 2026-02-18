class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        lookup = {}
        for i in s:
            lookup[i] = -1
        
        for i in range(len(s)):
            if lookup[ s[i] ] == -1 and t[i] not in set(lookup.values()):
                lookup[s[i]] = t[i]
            
            elif lookup[s[i]] != t[i]:
                return False
        
        return True