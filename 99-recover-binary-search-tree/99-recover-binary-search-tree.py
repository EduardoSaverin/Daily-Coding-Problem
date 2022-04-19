# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # Morris Traversal
        # If you get confused , especially with condition at Line 22, read
        # https://stackoverflow.com/questions/5502916/explain-morris-inorder-tree-traversal-without-using-stacks-or-recursion
        current, arr = root, []
        prev = TreeNode(-float("inf"))
        while current:
            if current.left is None:
                if prev.val > current.val:
                    arr += [prev, current]
                prev = current
                current = current.right
            else:
                pre = current.left
                while pre.right and pre.right != current:
                    pre = pre.right
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    if prev.val > current.val:
                        arr += [prev, current]
                    prev = current
                    current = current.right
        arr[0].val, arr[-1].val = arr[-1].val, arr[0].val
                        
                    
                
                        
            
        
        
            