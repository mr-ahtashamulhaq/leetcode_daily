class Solution:     
        
    def climbStairs(self, n):
        prev  = 1
        prev2 = 1
        curr = 1
        
        for num in range(2, n+1):
            curr = prev + prev2
            prev2 = prev
            prev = curr
        
        return curr