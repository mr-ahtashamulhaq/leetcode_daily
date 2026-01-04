class Solution:
    def dfs_algo(self, r, c, rows, cols, visited, board):
        if r<0 or c <0 or r>=rows or c >= cols:
            return
        if board[r][c] == "X":
            return
        if visited[r][c] == 1:
            return

        visited[r][c] = 1
        self.dfs_algo(r+1, c, rows, cols, visited, board)
        self.dfs_algo(r-1, c, rows, cols, visited, board)
        self.dfs_algo(r, c+1, rows, cols, visited, board)
        self.dfs_algo(r, c-1, rows, cols, visited, board)


    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows  = len(board)
        cols  = len(board[0])

        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        #Upper row
        r = 0
        for c in range(cols):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs_algo(r, c, rows, cols, visited, board)
             
        #Bottom row
        r = rows-1
        for c in range(cols):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs_algo(r, c, rows, cols, visited, board)

        #Left column
        c = 0
        for r in range(rows):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs_algo(r, c, rows, cols, visited, board)

        #Right Column
        c = cols-1
        for r in range(rows):
            if board[r][c] == "O":
                if visited[r][c] == 0:
                    self.dfs_algo(r, c, rows, cols, visited, board) 

        #changing in board
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O" and visited[r][c] == 0:
                    board[r][c] = "X"
