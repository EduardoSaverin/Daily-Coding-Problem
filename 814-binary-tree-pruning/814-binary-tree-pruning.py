# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        left = self.pruneTree(root.left)
        right = self.pruneTree(root.right)
        if not left:
            root.left = None
        if not right:
            root.right = None
        return root if left or right or root.val == 1 else None