class Solution(object):
    def largestOddNumber(self, num):
        """
        :type num: str
        :rtype: str
        """
        temp = int(num)
        while True:
            if temp%2 != 0:
                return str(temp)
            elif temp == 0:
                return ""
            else:
                temp = temp / 10
        