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
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def intReturn(root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> int:
            if subRoot is None:
                return 1
            if root is None:
                return 0
            if self.isSameTree(root, subRoot):
                return 1
            return intReturn(root.left, subRoot) + intReturn(root.right, subRoot)
        return intReturn(root, subRoot) >= 1