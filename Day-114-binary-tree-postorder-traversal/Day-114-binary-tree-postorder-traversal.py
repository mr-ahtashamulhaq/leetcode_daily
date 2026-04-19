# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def post_order(self, node, result):
        if node == None:
            return 
        self.post_order(node.left, result)
        self.post_order(node.right, result)
        result.append(node.val)
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        self.post_order(root, result)
        return result