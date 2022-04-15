# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        if not root or (root.left is None and root.right is None and (root.val < low or root.val > high)):
            return None
        if root.val < low:
            return self.trimBST(root.right, low, high)
        elif root.val > high:
            return self.trimBST(root.left, low, high)
        # Check for left value
        if root.left and root.left.val < low:
            root.left = self.trimBST(root.left.right, low, high)
        else:
            root.left = self.trimBST(root.left, low, high)
        # Check for right value
        if root.right and root.right.val > high:
            root.right = self.trimBST(root.right.left, low, high)
        else:
            root.right = self.trimBST(root.right, low, high)
        return root
            
            
         