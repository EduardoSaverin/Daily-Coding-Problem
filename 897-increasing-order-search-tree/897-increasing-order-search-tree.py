# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        values = []
        def recursion(root, values):
            if not root:
                return
            recursion(root.left, values)
            values.append(root.val)
            recursion(root.right, values)
        recursion(root, values)
        return self.build_skewed(values)

    def build_skewed(self, values):
        root = temp = None
        for value in values:
            node = TreeNode(value)
            if root is None:
                root = temp = node
            else:
                temp.right = node
                temp = node
        return root