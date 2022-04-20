# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: Optional[TreeNode]):
        self.root = root
        self.iter = iter(self._morris_traversal())
        self.next_val = next(self.iter, None)

    def next(self) -> int:
        val = self.next_val
        self.next_val = next(self.iter, None)
        return val

    def hasNext(self) -> bool:
        return self.next_val is not None
    
    def _morris_traversal(self):
        current = self.root
        while current:
            if current.left is None:
                yield current.val
                current = current.right
            else:
                pre = current.left
                while pre.right is not None and pre.right != current:
                    pre = pre.right
                if pre.right is None:
                    pre.right = current
                    current = current.left
                else:
                    pre.right = None
                    yield current.val
                    current = current.right
        


# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()