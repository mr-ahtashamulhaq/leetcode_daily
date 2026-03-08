class Solution:
    def minMovesToMakePalindrome(self, s: str) -> int:
        s = list(s)
        ans = 0
        lt = 0
        rt = len(s) - 1

        while lt < rt:

            i = rt
            j = rt

            while i > lt and s[i] != s[lt]:
                i -= 1

            if i == lt:
                s[i], s[i+1] = s[i+1], s[i]
                ans += 1
            else:
                while i < j:
                    s[i], s[i+1] = s[i+1], s[i]
                    ans += 1
                    i += 1

                lt += 1
                rt -= 1

        return ans