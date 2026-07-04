# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        q = []
        output = []
        q.append(root)
        while q:
            rightMost = 0
            for node in range(len(q)):
                qNode = q.pop(0)
                if qNode.left is not None:
                    q.append(qNode.left)
                if qNode.right is not None:
                    q.append(qNode.right)
                rightMost = qNode.val
            output.append(rightMost)
        return output

        