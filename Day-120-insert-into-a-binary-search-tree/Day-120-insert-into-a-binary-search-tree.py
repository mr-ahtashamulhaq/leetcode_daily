# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        val_node = TreeNode(val)
        if root is None:
            return val_node

        temp = root
        
        while True:
            if val < temp.val:
                if temp.left is None:
                    temp.left = val_node
                    break
                temp = temp.left
            else:
                if temp.right is None:
                    temp.right = val_node
                    break
                temp = temp.right

        return root