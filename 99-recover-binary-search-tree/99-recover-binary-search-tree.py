# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.first = None
        self.second = None
        self.prev = TreeNode(-float("inf"))
        self.traverse(root)
        self.first.val, self.second.val = self.second.val, self.first.val
    
    def traverse(self, root):
        if not root:
            return
        self.traverse(root.left)
        if self.first is None and self.prev.val >= root.val:
            self.first = self.prev
        if self.first is not None and self.prev.val >= root.val:
            self.second = root
        self.prev = root
        self.traverse(root.right)
            
        
        
            