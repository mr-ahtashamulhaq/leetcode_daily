class Solution:
    def sumOfSquareOfDigit(self, n):
        output = 0

        while n:
            digit = n % 10
            digit = digit ** 2
            output += digit
            n = n//10
        
        return output


    def isHappy(self, n: int) -> bool:
        slow = fast = n

        while(fast != 1):
            slow = self.sumOfSquareOfDigit(slow)
            fast = self.sumOfSquareOfDigit(fast)
            fast = self.sumOfSquareOfDigit(fast)

            if fast == 1:
                return True
            if slow == fast:
                return False
        
        return True
            