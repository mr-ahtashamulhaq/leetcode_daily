class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix:
            return []

        result = []
        top, left = 0, 0
        bottom, right = len(matrix) - 1, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # from Left to Right
            for i in range(left, right + 1):
                result.append(matrix[top][i])
            top += 1

            # from Top to Bottom
            for i in range(top, bottom + 1):
                result.append(matrix[i][right])
            right -= 1

            # from Right to Left
            if top <= bottom:
                for i in range(right, left - 1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            # from Bottom to Top
            if left <= right:
                for i in range(bottom, top - 1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result