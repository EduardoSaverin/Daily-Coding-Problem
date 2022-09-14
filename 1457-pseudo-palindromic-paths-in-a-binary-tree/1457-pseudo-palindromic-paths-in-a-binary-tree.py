class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        return self.dfs(root)
    
    def dfs(self, root, s = set()):
        if not root:
            return 0
        s.remove(root.val) if root.val in s else s.add(root.val)
        count = 0
        if not root.left and not root.right:
            # If set is empty then it is even plaindrome -> no swap required
            # If set has 1 element, it is odd plaindrome -> count it
            # if set has > 1 element, then it is not plaindrome -> reject
            if len(s) <= 1:
                count = 1
        else:
            count += self.dfs(root.left, s) + self.dfs(root.right, s)
        # Again removing since element may be added in subtree
        s.remove(root.val) if root.val in s else s.add(root.val)
        return count
    
            
        