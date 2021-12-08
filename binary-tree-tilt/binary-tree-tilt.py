# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        def recursion(root):
            if root is None:
                return 0
            left = recursion(root.left)
            right = recursion(root.right)
            root.sum = abs(left-right)
            return root.val + left + right
        recursion(root)
        def getsum(root):
            if root is None:
                return 0
            left = getsum(root.left)
            right = getsum(root.right)
            return root.sum + left + right
        return getsum(root)