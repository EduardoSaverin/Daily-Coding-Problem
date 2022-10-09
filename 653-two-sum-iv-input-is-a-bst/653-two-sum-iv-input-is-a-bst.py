# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], target: int) -> bool:
        d = defaultdict(int)
        def traverse(root):
            if not root:
                return False
            remain = target - root.val
            if remain in d and d[remain] > 0:
                return True
            d[root.val] += 1 
            return traverse(root.left) or traverse(root.right)
        return traverse(root)
            