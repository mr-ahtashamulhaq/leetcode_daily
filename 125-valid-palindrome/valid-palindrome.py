class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        s = s.lower()
        while i < j :
            if s[i] != s[j]:
                if s[i].isalnum() and s[j].isalnum():
                    return False
                if s[i].isalnum() != True:
                    i+=1
                if s[j].isalnum() != True:
                    j-=1
            else:
                i+=1
                j-=1
        return True

