class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adj_list = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for u ,v in prerequisites:
            adj_list[v].append(u)
            indegree[u] +=1
        
        result = []
        queue = deque()
        for i in range(0 ,numCourses):
            if indegree[i] == 0:
                queue.append(i)
            
        while queue:
            node  = queue.popleft()
            result.append(node)
            
            for adjNode in adj_list[node]:
                indegree[adjNode] -=1
                if indegree[adjNode]== 0:
                    queue.append(adjNode)
                
        if len(result) == numCourses:
            return result
        return []