# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = [root, "$"]
        levels = []
        current_level = []
        while q:
            node = q.pop(0)
            if node == "$":
                if len(q) != 0:
                    q.append("$")
                levels.append(current_level)
                current_level = []
                continue
            current_level.append(node.val)
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return levels