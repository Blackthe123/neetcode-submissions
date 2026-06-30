# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def traverse(p: Optional[TreeNode], q: Optional[TreeNode])->int:
            if (p is None and q is not None) or (p is not None and q is None):
                return 0 
            elif (p is None and q is None):
                return 1
            elif p.val != q.val:
                return 0
            return traverse(p.left, q.left) * traverse(p.right, q.right)
        return traverse(p, q) == 1