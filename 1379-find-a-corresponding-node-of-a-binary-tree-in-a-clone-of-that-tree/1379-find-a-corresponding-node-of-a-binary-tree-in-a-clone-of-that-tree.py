# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.target = target
        node1 = self.getNode(original)
        node2 = self.getNode(cloned)
        if self.isSame(node1, node2):
            return node2
        return target
    
    def getNode(self, root):
        if root is None:
            return
        if root.val == self.target.val:
            return root
        return self.getNode(root.left) or self.getNode(root.right)
        
    def isSame(self, root1: TreeNode, root2: TreeNode) -> bool:
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        return root1.val == root2.val and self.isSame(root1.left, root2.left) and self.isSame(root1.right, root2.right)