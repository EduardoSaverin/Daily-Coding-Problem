# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        return self.dfs(root, root.val)
    
    def dfs(self, root, val):
        if root is None:
            return 0
        result = 1 if root.val >= val else 0
        if root.left:
            result += self.dfs(root.left, max(root.val, val))
        if root.right:
            result += self.dfs(root.right, max(root.val, val))
        return result
        