# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def dfs(self, Node, curr):
        if Node is None:
            return 0

        curr = curr * 2 + Node.val

        if not Node.left and not Node.right:
            return curr

        return self.dfs(Node.left, curr) + self.dfs(Node.right, curr)

    def sumRootToLeaf(self, root):
        return self.dfs(root, 0)