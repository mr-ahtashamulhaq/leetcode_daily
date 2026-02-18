class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        n = len(s)
        rotate = s

        for i in range(n):
            if rotate == goal:
                return True
            else:
                rotate = rotate[-1] + rotate[:-1]

        return False