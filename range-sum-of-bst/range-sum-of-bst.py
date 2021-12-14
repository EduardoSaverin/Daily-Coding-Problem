# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        result = 0
        def recursion(root):
            nonlocal result
            if root is None:
                return 0
            recursion(root.left)
            if low <= root.val and root.val <= high:
                result += root.val
            recursion(root.right)
        recursion(root)
        return result