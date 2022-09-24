# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        self.target = targetSum
        self.result = []
        self.dfs(root, 0 , [])
        return self.result
    
    def dfs(self, node, total = 0, path = []):
        if not node:
            return
        total += node.val
        path.append(node.val)
        if total == self.target and not node.left and not node.right:
            self.result.append(path)
            return
        self.dfs(node.left, total, path[::])
        self.dfs(node.right, total, path[::])