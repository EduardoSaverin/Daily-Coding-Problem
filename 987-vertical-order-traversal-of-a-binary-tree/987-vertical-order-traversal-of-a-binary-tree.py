# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.map = defaultdict(dict)
        root.row = 0
        root.col = 0
        self.traverse(root)
        keys = sorted(self.map.keys())
        result = []
        for key in keys:
            temp = []
            new_keys = sorted(self.map[key].keys())
            for k in new_keys:
                temp.extend(sorted(self.map[key][k]))
            result.append(temp)
        return result
        
    def traverse(self, root):
        if not root:
            return
        d = self.map[root.col]
        if root.row not in d:
            d[root.row] = []
        d[root.row].append(root.val)
        if root.left:
            root.left.row = root.row + 1
            root.left.col = root.col - 1
            self.traverse(root.left)
        if root.right:
            root.right.row = root.row + 1
            root.right.col = root.col + 1
            self.traverse(root.right)
        
        