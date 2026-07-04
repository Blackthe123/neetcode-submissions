# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        def countNodes(root, maxSoFar):
            if root is None:
                return 0
            count = 0
            if root.val >= maxSoFar:
                count = 1
                maxSoFar = root.val
            return count + countNodes(root.left, maxSoFar) + countNodes(root.right, maxSoFar)
        return countNodes(root, root.val)
        
        