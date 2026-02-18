class Solution(object):
    def reverseBits(self, n):
        """
        :type n: int
        :rtype: int
        """
        result = 0
        for i in range(32):
            bit = n & 1
            result = result << 1
            result = result | bit
            n = n >> 1

        return result 