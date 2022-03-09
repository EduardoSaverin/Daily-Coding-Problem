# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        result = float("inf")
        minimum = root.val
        def traverse(root):
            nonlocal result, minimum
            if root is None:
                return
            if result > root.val and minimum < root.val:
                result = root.val
            else:
                traverse(root.left)
                traverse(root.right)
        traverse(root)
        return result if result != float("inf") else -1
            