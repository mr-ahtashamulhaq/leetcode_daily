class Solution:
    def findContentChildren(self, g, s) :
        right = 0
        left = 0
        count = 0
        s.sort()
        g.sort()
        while right < len(s) and left < len(g):
            if g[left] <= s[right]:
                count +=1
                left +=1
            right +=1


        return count