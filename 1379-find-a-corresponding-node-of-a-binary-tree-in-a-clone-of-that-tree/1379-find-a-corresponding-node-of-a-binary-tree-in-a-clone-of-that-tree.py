# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        def recursion(root1, root2):
            if root1:
                recursion(root1.left, root2.left)
                if root1 is target:
                    self.ans = root2
                recursion(root1.right, root2.right)
        recursion(original, cloned)
        return self.ans