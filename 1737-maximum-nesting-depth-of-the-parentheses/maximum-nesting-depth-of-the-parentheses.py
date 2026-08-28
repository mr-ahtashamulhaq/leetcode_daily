class Solution:
    def maxDepth(self, s: str) -> int:
        count = 0
        temp = 0
        for i in s:
            if i == "(":
                temp +=1
            if i == ")":
                temp -=1
            
            count = max(count, temp)
        return count
            