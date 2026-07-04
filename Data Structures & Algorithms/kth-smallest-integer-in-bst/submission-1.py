# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def __init__(self):
        self.count = 0
        self.value = 0
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if root is None:
            return 0
        self.kthSmallest(root.left, k)
        self.count += 1
        if self.count == k:
            self.value = root.val
        self.kthSmallest(root.right, k)
        return self.value


        