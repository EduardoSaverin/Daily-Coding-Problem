# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        q = []
        q.append([root, 0, 0])
        current_depth = 0
        left = 0
        result = 0
        while q:
            node, depth, position = q.pop(0)
            if node:
                q.append([node.left, depth+1, position*2])
                q.append([node.right, depth+1, position*2+1])
                if current_depth != depth:
                    current_depth = depth
                    left = position
                # R-L+1 <-- Width of each level
                result = max(result, (position-left+1))
        return result