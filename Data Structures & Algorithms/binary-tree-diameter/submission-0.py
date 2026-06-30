# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.diameter = 0
    def heightOfTree(self, root) -> int:
        if root is None:
            return 0
        left = 1 + self.heightOfTree(root.left)
        right = 1 + self.heightOfTree(root.right)
        if left > right:
            return left
        else:
            return right
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        curr = self.heightOfTree(root.left) + self.heightOfTree(root.right)
        if curr > self.diameter:
            self.diameter = curr
        self.diameterOfBinaryTree(root.left)
        self.diameterOfBinaryTree(root.right)
        return self.diameter