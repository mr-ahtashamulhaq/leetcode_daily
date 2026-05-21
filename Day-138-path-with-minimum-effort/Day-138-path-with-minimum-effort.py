class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        rows  = len(heights)
        cols  = len(heights[0])
        effort = [[float("inf") for _ in range(cols)] for _ in range(rows)]
        
        priority_q = []
        priority_q.append([0 , 0 ,0 ])
        effort[0][0] = 0

        while priority_q:
            curr_eff , r , c = heapq.heappop(priority_q)

            if r == rows-1 and c == cols-1:
                return curr_eff

            for x, y in [[0,1] , [0,-1] , [1, 0] , [-1,0]]:
                new_r = r + x
                new_c = c + y

                if new_r < 0 or new_r >=rows or new_c<0 or new_c>=cols:
                    continue
                
                new_eff = max( curr_eff , abs(heights[r][c] - heights[new_r][new_c]))

                if new_eff < effort[new_r][new_c]:
                    effort[new_r][new_c] = new_eff
                    heapq.heappush(priority_q , [new_eff , new_r , new_c])
        
        