# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        output = []
        q = []
        if root is None:
            return output
        q.append(root)
        currLevel = 0
        while q:
            subList = []
            for node in range(len(q)):
                qNode = q.pop(0)
                if qNode.left is not None:
                    q.append(qNode.left)
                if qNode.right is not None:
                    q.append(qNode.right)
                subList.append(qNode.val)
            output.append(subList)
        return output
        