# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        return self.insert(root, val)
    
    def insert(self, root: Optional[TreeNode], value: int) -> Optional[TreeNode]:
        if root is None:
            return TreeNode(value)
        if value < root.val:
            root.left = self.insert(root.left, value)
        if value > root.val:
            root.right = self.insert(root.right, value)
        return root