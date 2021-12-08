# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    result = 0
    def findTilt(self, root: Optional[TreeNode]) -> int:
        result = 0
        def recursion(root):
            nonlocal result
            if root is None:
                return 0
            left = recursion(root.left)
            right = recursion(root.right)
            root.sum = abs(left-right)
            result += root.sum
            return root.val + left + right
        recursion(root)
        return result
