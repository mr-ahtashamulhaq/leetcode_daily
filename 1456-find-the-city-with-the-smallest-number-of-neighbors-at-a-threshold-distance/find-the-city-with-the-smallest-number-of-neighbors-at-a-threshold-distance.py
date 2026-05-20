class Solution:
    def findTheCity(self, n: int, edges, distanceThreshold: int) -> int:
        adj_matrix = [[float("inf") for _ in range(n)] for _ in range(n)]

        for u, v, w in edges:
            adj_matrix[u][v] = w
            adj_matrix[v][u] = w
        
        for i in range(n):
            adj_matrix[i][i] = 0

        n = len(adj_matrix)
        for via in range(n):
            for i in range(n):
                for j in range(n):
                    if adj_matrix[i][via] != 10**8 and adj_matrix[via][j] != 10**8:
                        adj_matrix[i][j] = min(
                            adj_matrix[i][j], adj_matrix[i][via] + adj_matrix[via][j])

        neighbour = n
        result = -1

        for i in range(n):
            count = 0
            for j in range(n):
                if adj_matrix[i][j] <= distanceThreshold:
                    count += 1

            if count <= neighbour:
                neighbour = count
                result = i
        return result