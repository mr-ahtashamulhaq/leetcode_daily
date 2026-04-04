class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:

        V1 = version1.split(".")
        V2 = version2.split(".")
        n1 = len(V1)
        n2 = len(V2)

        i = 0
        j = 0
        while i < n1 or j < n2:

            if i >= n1 :
                val1 = 0
            else:
                val1 = int(V1[i])
            
            if j >= n2:
                val2 = 0
            else:
                val2 = int(V2[j]) 

            if val1 == val2 :
                if i == n1-1 and j== n2-1:
                    return 0
                    continue
            elif val1 < val2 :
                return -1

            elif val1 > val2 :
                return 1
            
            i +=1
            j+=1
        return 0
                
