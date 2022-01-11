# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        result = []
        self.traverse(root, '' , result)
        return sum(result)
    
    def traverse(self, root, num, sums=[]):
        if root is None:
            return
        num += str(root.val)
        if not root.left and not root.right:
            sums.append(int(num,2))
        else:
            if root.left:
                self.traverse(root.left, num, sums)
            if root.right:
                self.traverse(root.right, num, sums)
            