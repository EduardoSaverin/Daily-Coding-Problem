# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: TreeNode, to_delete: List[int]) -> List[TreeNode]:
        forest = []
        def recursion(root, is_root=False):
            if not root:
                return None
            
            if root.val in to_delete:
                recursion(root.left, True)
                recursion(root.right, True)
                return None
            else:
                root.left = recursion(root.left)
                root.right = recursion(root.right)
            if is_root:
                forest.append(root)
            return root
        
        recursion(root, True)
        return forest