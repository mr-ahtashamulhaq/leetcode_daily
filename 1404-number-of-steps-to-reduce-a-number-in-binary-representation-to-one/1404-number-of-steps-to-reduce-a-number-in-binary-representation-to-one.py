class Solution:
    def numSteps(self, s: str) -> int:
        count = 0
        num = int(s, 2)
        
        while True:
            if num == 1:
                return count
            count +=1
            if num %2 == 0:
                num = num //2
            elif num %2 != 0:
                num +=1
