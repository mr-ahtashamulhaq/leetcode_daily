class Solution:
    def countPaths(self, n: int, roads: List[List[int]]) :
        
        adj_list = [[] for _ in range(n)]
        MOD = 10**9 +7
        for u , v , weight in roads:
            adj_list[u].append([v ,weight])
            adj_list[v].append([u ,weight])

        ways  = [0  for _ in range(n)]
        distance = [float("inf") for _ in range(n)]
        distance[0] = 0
        ways[0] = 1         # --> we have 1 number of ways to reach at 0 

        priority_q = []
        priority_q.append([0 , 0])      # [Dist , Node]

        while priority_q:
            dist , node = heapq.heappop(priority_q)

            for adjNode , weight in adj_list[node]:
                new_dist = dist + weight

                if new_dist < distance[adjNode]:
                    distance[adjNode] = new_dist
                    heapq.heappush(priority_q , [new_dist , adjNode]) 
                    ways[adjNode] = ways[node]

                elif new_dist == distance[adjNode]:
                    ways[adjNode] += ways[node]

        return ways[n-1] % MOD