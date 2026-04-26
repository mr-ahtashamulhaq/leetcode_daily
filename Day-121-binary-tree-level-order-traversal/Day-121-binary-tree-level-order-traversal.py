class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[Node]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([])
        queue.append(root)

        while queue:
            current_level = []
            size  = len(queue)

            for i in range(size):
                e = queue.popleft()
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
                current_level.append(e.val)
            result.append(current_level)
        return result