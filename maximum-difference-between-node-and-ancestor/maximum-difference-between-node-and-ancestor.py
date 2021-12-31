# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        maxDiff = 0
        q = [root]    
        while q:
            node = q.pop(0)
            anc = []
            self.get_ancestor(root, node.val, anc)
            # print(anc)
            for n in anc:
                maxDiff = max(maxDiff, abs(n-node.val))
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return maxDiff
    
    def get_ancestor(self, root, target, nodes=[]):
        if root is None:
            return False
        if root.val == target:
            return True
        if self.get_ancestor(root.left, target, nodes) or self.get_ancestor(root.right, target, nodes):
            nodes.append(root.val)
            return True
        return False
        