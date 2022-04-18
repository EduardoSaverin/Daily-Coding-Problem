# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        l = [0]
        result = root.val
        def traverse(root, l):
            nonlocal result
            if root is None:
                return
            traverse(root.left, l)
            l[0] = l[0]+1
            if l[0] == k:
                result = root.val
                return
            traverse(root.right, l)
        traverse(root, l)
        return result