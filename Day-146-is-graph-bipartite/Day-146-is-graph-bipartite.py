class Solution:
    def dfs_algo(self, graph , visited , node, color):
        visited[node]  = color

        for n in graph[node]:
            if visited [n] != -1:

                #0 ,1
                if visited[n] == color:
                    return False

            else:
                if color == 0:
                    ans  = self.dfs_algo(graph, visited, n, 1)
                else:
                    ans  = self.dfs_algo(graph, visited, n, 0)

                if ans == False:
                    return False
        return True

    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [-1 for _ in range(n)]

        for i in range(n):
            if visited[i] == -1:
                ans = self.dfs_algo(graph  , visited , i , 0)
                if ans ==False:
                    return False
        return True