class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        col = len(grid[0])

        grid_copy = deepcopy(grid)
        queue = deque()
        fresh = 0

        for i in range(rows):
            for j in range(col):
                if grid_copy[i][j] == 2:
                    queue.append((i,j))
                elif grid_copy[i][j] == 1:
                    fresh +=1
        minute = 0
        while len(queue) != 0 and fresh > 0:
            minute +=1
            total_rotten = len(queue)
            for _ in range(total_rotten):
                i , j = queue.popleft()

                for dx , dy in [(-1 , 0), (1, 0) , (0 ,-1) , (0, 1)]:
                    new_i , new_j = i + dx , j + dy

                    if new_i < 0 or new_j < 0 or new_i == rows or new_j == col:
                        continue
                    elif grid_copy[new_i][new_j] == 0 or grid_copy[new_i][new_j]== 2:
                        continue
                    
                    fresh -=1
                    grid_copy[new_i][new_j] = 2
                    queue.append((new_i , new_j))
        
        if fresh > 0:
            return -1
        return minute