# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.camera = 0
        value = self.dfs(root)
        return self.camera + (1 if value == 2 else 0)
    
    def dfs(self, root):
        # NULL is monitored
        if root is None:
            return 1
        left = self.dfs(root.left)
        right = self.dfs(root.right)
        
        # Both are monitored, no monitoring required
        if left == 1 and right == 1:
            return 2
        
        # One of the child is not monitored
        if left == 2 or right == 2:
            self.camera += 1
            return 3
        return 1