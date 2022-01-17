# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0
        def recursion(root):
            nonlocal result
            if not root:
                return 0
            left = 0
            if root.left:
                left = recursion(root.left) + 1
            right = 0
            if root.right:
                right = recursion(root.right) + 1
            temp = max(left,right)
            if left+right > result:
                result = left+right
            return temp
        recursion(root)
        return result