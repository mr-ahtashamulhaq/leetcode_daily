# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        temp = root

        while temp is not None:
            if val == temp.val:
                return temp
            elif val < temp.val:
                temp = temp.left
            else:
                temp = temp.right
        return None