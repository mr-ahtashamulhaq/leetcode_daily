class Solution:
    def solve(self, curr:list, result, n):
        if len(curr) == n:
            result.append("".join(curr))
            return
        
        for ch in ["a", "b", "c"]:
            if len(curr) != 0 and curr[-1] == ch:
                continue
            curr.append(ch)

            self.solve(curr, result, n)
            curr.pop()
        
        
        
            

    def getHappyString(self, n: int, k: int) -> str:
        curr = []
        result = []
        self.solve(curr, result, n)

        if len(result) < k :
            return ""
        return result[k-1]
        