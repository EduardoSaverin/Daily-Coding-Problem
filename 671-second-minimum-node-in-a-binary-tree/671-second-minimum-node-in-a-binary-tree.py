# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        s = set()
        def traverse(root):
            if root is None:
                return
            s.add(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        l = list(s)
        l.sort()
        return -1 if len(l) < 2 else l[1]
            