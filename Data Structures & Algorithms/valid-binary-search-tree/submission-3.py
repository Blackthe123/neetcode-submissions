# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = [-float('inf')]
        def inOrder(root, prev):
            if root is None:
                return True
            if not inOrder(root.left, prev):
                return False
            if root.val <= prev[0]:
                return False
            else:
                prev[0] = root.val
            return inOrder(root.right, prev)
        return inOrder(root, prev)



        