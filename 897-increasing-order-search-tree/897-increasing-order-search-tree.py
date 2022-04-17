# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def recursion(root):
            if not root:
                return
            recursion(root.left)
            root.left = None
            self.current.right = root
            self.current = root
            recursion(root.right)
        head = self.current = TreeNode()
        recursion(root)
        return head.right
            