# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self,Node, temp):
        if Node is None:
            return 0

        if not Node.left and not Node.right:
            return int(temp[::-1] + str(Node.val), 2) 

        left = self.dfs(Node.left, str(Node.val) + temp)
        right =self.dfs(Node.right, str(Node.val) + temp)

        return left + right
        
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, "")