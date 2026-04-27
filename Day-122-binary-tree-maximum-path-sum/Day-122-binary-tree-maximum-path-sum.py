# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    total_sum = 0
    def checker (self, node ):
        if node==None:
            return 0

        left_sum = self.checker(node.left)
        if left_sum < 0:
            left_sum = 0

        right_sum = self.checker(node.right)
        if right_sum < 0:
            right_sum = 0

        self.total_sum = max(self.total_sum , left_sum + right_sum + node.val)

        return  node.val + max(left_sum , right_sum)


    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.total_sum =float("-inf")
        self.checker(root)
        return self.total_sum