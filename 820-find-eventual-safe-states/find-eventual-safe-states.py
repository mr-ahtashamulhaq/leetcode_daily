class Solution:
    # -------- helper DFS ----------
    def dfs(self, current_node, adj_list, vis, path_vis, is_safe):
        vis[current_node] = 1       
        path_vis[current_node] = 1   

        for adjNode in adj_list[current_node]:
            if vis[adjNode] == 0:                    
                ans = self.dfs(adjNode, adj_list, vis, path_vis, is_safe)
                if ans == False:                    
                    return False
            elif path_vis[adjNode] == 1:            
                return False                         

        path_vis[current_node] = 0   
        is_safe[current_node] = 1    
        return True

    # -------- main function ----------
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        V = len(graph)
        vis       = [0 for _ in range(V)]   # not processed yet
        path_vis  = [0 for _ in range(V)]   # not on current path
        is_safe   = [0 for _ in range(V)]   # 0 =  unsafe

        # launch DFS fro every unvisited node
        for i in range(V):
            if vis[i] == 0:
                self.dfs(i, graph, vis, path_vis, is_safe)

        # collect all nodes proven safe
        result = []
        for i in range(V):
            if is_safe[i] == 1:
                result.append(i)
        return result