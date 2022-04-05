# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def recursion(root, floor = -float("inf"), ceil = float("inf")):
            if root is None:
                return True
            if root.val <= floor or root.val >= ceil:
                return False
            return recursion(root.left, floor , root.val) and recursion(root.right, root.val, ceil)
        return recursion(root)
            