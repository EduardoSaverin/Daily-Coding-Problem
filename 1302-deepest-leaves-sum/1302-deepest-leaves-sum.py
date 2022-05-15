# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        total = 0
        temp = 0
        q = deque()
        q.append(root)
        q.append("#")
        while q:
            node = q.popleft()
            if node == '#':
                total = temp
                temp = 0
                if len(q) != 0:
                    q.append("#")
                continue
            temp += node.val
            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
        return total
            
                    
            
        