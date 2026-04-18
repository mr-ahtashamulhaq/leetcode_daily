class Solution:
    def maxScore(self, cardpoints: List[int], k: int) -> int:
        n = len(cardpoints)
        if n==k:
            return sum(cardpoints)
        right_sum = 0

        left_sum = sum(cardpoints[:k])

        result = left_sum
        right_index = n-1

        for i in range(k-1, -1,-1):
            left_sum -= cardpoints[i]
            right_sum += cardpoints[right_index]

            total = left_sum + right_sum
            result = max(result, total)

            right_index -=1
        return result