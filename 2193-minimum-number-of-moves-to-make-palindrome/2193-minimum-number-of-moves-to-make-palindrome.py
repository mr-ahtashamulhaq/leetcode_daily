class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        ans = 0
        lt = 0
        rt = len(s) -1
        while lt < rt:

            i = rt
            j = rt

            while i > lt and s[i] != s[lt]: #Move left pointer forward until found same element
                i-=1
            
            if i == lt :
                s[i], s[i+1] = s[i+1], s[i]
                ans += 1
            
            else:
                while i  < j:
                    s[i], s[i+1] = s[i+1], s[i]
                    i += 1
                    ans += 1

                lt += 1
                rt -= 1
        return ans