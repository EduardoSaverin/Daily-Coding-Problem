# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.result = 0
        self.dfs(root)
        return self.result
    
    def dfs(self, root):
        if root is None:
            return 0
        left, right = self.dfs(root.left) , self.dfs(root.right)
        self.result += abs(left) + abs(right)
        return root.val + left + right - 1