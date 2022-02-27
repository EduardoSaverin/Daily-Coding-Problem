# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        # .
        if root is None:
            return True
        q = [[root.left, root.right]]
        while q:
            left, right = q.pop(0)
            if left is None and right is None:
                continue
            elif left is None or right is None:
                return False
            elif left.val != right.val:
                return False
            else:
                q.append([left.right, right.left])
                q.append([left.left, right.right])
        return True
            