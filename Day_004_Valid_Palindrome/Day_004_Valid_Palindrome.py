# 125. Valid Palindrome
"""
A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

Given a string s, return true if it is a palindrome, or false otherwise.
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:

        i = 0
        j = len(s) - 1
        s = s.lower()
        while i <= j:
            if s[i] != s[j]:
                if s[i].isalnum() == True and s[j].isalnum() == True:
                    return False
                elif s[i].isalnum() == False:
                    i += 1
                    continue
                elif s[j].isalnum() == False:
                    j -= 1
                    continue
            i += 1
            j -= 1

        return True


obj = Solution()
s = "A man, a plan, a canal: Panama"
print(obj.isPalindrome(s))

# Output : True