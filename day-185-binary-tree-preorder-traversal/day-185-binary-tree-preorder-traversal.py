# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pre_order(self,node, result):
        if node == None:
            return 
        result.append(node.val)
        self.pre_order(node.left, result)
        self.pre_order(node.right, result)
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        self.pre_order(root,result)
        return result