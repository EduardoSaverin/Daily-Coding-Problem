# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []
        END = "$"
        q = [root, END]
        result = []
        prev = None
        s = 0
        count = 0
        while q:
            node = q.pop(0)
            if node == END and prev == END:
                continue
            if node == END:
                result.append(s/count)
                count = 0
                s = 0
                q.append(END)
                prev = node
                continue
            count += 1
            s += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
            prev = node
        return result
        