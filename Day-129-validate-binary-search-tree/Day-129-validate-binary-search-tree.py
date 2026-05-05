# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def solver  (self ,root,  limit ):
        if root == None:
            return True
        if not limit[0] < root.val < limit[1]:
            return False

        left = self.solver(root.left , [limit[0] , root.val])
        if left ==False:
            return False

        right = self.solver(root.right ,[root.val ,limit[1]])
            
        return left and right

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        limit = [float("-inf") , float("inf")]
        return self.solver(root, limit)