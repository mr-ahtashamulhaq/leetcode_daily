# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def checker(self, root):
        if root is None:
            return 0   

        left_depth = self.checker(root.left)
        # if left is un-balanced no need to check further
        if left_depth == -1:
            return -1

        right_depth = self.checker(root.right)
        # if right is un-balanced no need to check further
        if right_depth ==-1:
            return -1
        # if this one is unbalanced no need to check further
        if abs(left_depth - right_depth ) > 1:
            return -1

        return 1 + max(left_depth, right_depth)

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = self.checker(root)
        return False if result == -1 else True
        