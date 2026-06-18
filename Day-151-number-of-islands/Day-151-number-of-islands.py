class Solution:
    def bfs_algo(self, i, j, visited, grid):
        rows = len(grid)
        cols = len(grid[0])

        queue = deque()
        queue.append((i , j))
        visited[i][j] =1
        while queue:
            r, c = queue.popleft()

            for x , y in [(0,-1), (0, 1), (1, 0), (-1, 0)]:
                new_r = r+x
                new_c = c + y

                if new_r < 0 or new_c <0 or new_r >=rows or new_c >= cols:
                    continue
                if grid[new_r][new_c] == "0":
                    continue
                if visited[new_r][new_c]==1:
                    continue
                visited[new_r][new_c] = 1
                queue.append((new_r, new_c))

    def numIslands(self, grid: List[List[str]]) -> int:
        rows = len(grid)
        cols = len(grid[0])
        count = 0
        visited = [[0 for _ in range(cols)] for _ in range(rows)]

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and visited [r][c]==0:
                    count +=1
                    self.bfs_algo(r, c, visited, grid)

        return count