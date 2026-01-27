class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        row  = len(matrix)
        col = len(matrix[0])
        row_track = [0] * row
        col_track = [0] * col

        for i in range(row):
            for j in range(col):
                if matrix [i][j] == 0:
                    row_track[i] = -1
                    col_track[j] = -1
        
        for i in range(row): 
            for j in range(col):
                if row_track[i] == -1 or col_track[j] == -1:
                    matrix[i][j] = 0