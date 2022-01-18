# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.result = root.val
        self.traverse(root)
        return self.result
    
    def traverse(self, root):
        if not root:
            return 0
        left = self.traverse(root.left)
        right = self.traverse(root.right)
        self.result = max(self.result, max(left,0) + max(right,0) + root.val)
        return max(max(left,0), max(right,0)) + root.val
        