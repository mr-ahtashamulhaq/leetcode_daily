class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) -1
        count = 1
        while i < j:
            if s[i] == s[j]:
                i +=1
                j -=1
            else :
                s1 = s[i+1: j+1] #Skip left char
                s2 = s[i:j]
                if s1 == s1[::-1] or s2 == s2[::-1]:
                    return True
                else:
                    return False    
        return True
                
