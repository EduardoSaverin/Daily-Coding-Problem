# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        q = [root, "$"]
        result = []
        prev = None
        while q:
            node = q.pop(0)
            if node == "$":
                if prev is not None:
                    result.append(prev.val)
                if len(q) > 0:
                    prev = None
                    q.append("$")
                continue
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            prev = node
        return result