class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans = start ^ goal
        count =0
        for i in range(0,32):
            if (ans>>i) & 1 ==1:
                count +=1
        return count