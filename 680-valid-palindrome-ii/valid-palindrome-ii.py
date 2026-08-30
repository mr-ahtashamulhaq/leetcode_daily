class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        i = 0
        j = len(s) - 1
        while i < j:
            if(s[i] != s[j]):
                a = s[i+1:j+1:]
                b = s[i:j:]
                print("a", a)
                print("b",b)
                return True if ((a==a[::-1]) or (b == b[::-1])) else False
            i+=1
            j-=1
        return True