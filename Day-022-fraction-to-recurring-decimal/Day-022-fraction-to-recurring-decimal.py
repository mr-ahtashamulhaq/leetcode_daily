class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        if numerator == 0:
            return "0"
        
        result = []
        
        # add negative if only 1 is negative
        if (numerator < 0) ^ (denominator < 0):
            result.append("-")
        

        numerator = abs(numerator)
        denominator = abs(denominator)
        
        result.append(str(numerator // denominator))
        numerator = numerator % denominator
        
        if numerator == 0:
            return "".join(result)

        result.append(".")
        seen = {}
        while numerator != 0:
            
            if numerator in seen:
                index = seen[numerator]
                result.insert(index , "(")
                result.append(")")
                break


            seen[numerator] = len(result)
            numerator *= 10
            result.append(str(numerator // denominator))
            numerator = numerator % denominator

        return "".join(result)