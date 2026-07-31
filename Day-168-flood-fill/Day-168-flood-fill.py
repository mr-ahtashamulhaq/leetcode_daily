class Solution:
    def flood_fill_DFS(self, i ,j , new_color , initial_color, visited, rows , cols):
        if i < 0 or j < 0 or i == rows or j == cols:
            return
        if visited[i][j] != initial_color:
            return
        if visited[i][j] == initial_color:
            visited[i][j] = new_color

        self.flood_fill_DFS(i+1 ,j   , new_color, initial_color, visited, rows, cols)
        self.flood_fill_DFS(i-1 ,j   , new_color, initial_color, visited, rows, cols)
        self.flood_fill_DFS(i   ,j-1 , new_color, initial_color, visited, rows, cols)
        self.flood_fill_DFS(i   ,j+1 , new_color, initial_color, visited, rows, cols)



    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image
                
        visited = deepcopy(image)
        rows = len(visited)
        cols = len(visited[0])
        original_color = visited[sr][sc]


        self.flood_fill_DFS( sr , sc , color , original_color ,visited, rows , cols )
        return visited