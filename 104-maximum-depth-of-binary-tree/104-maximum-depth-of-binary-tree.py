# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        result = 0
        def recursion(root, depth):
            nonlocal result
            if root is None:
                if depth > result:
                    result = depth
                return
            recursion(root.left, depth+1)
            recursion(root.right, depth+1)
        recursion(root, 0)
        return result