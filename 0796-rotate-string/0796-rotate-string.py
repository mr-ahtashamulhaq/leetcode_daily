class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        rotate = s[-1] + s[:n-1]

        for i in range(n):
            # print(rotate)
            if rotate == goal:
                return True
            else:
                rotate = rotate[-1] + rotate[:n-1]

        return False