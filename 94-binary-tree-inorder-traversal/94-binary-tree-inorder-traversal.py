# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        l = []
        def traverse(root, l):
            if root is None:
                return
            traverse(root.left, l)
            l.append(root.val)
            traverse(root.right, l)
        traverse(root, l)
        return l