# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0
        def recursion(node, maximum, minimum):
            nonlocal result
            if not node:
                return
            result = max(result, abs(maximum-node.val), abs(minimum-node.val))
            minimum = min(minimum, node.val)
            maximum = max(maximum, node.val)
            recursion(node.left, maximum, minimum)
            recursion(node.right, maximum, minimum)
        recursion(root, root.val, root.val)
        return result