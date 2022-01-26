# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        list1 = []
        list2 = []
        self.traverse(root1,list1)
        self.traverse(root2, list2)
        return self.merge(list1, list2)
    
    def merge(self, list1, list2):
        result = []
        length1 = len(list1)
        length2 = len(list2)
        i = 0
        j = 0
        while i < length1 and j < length2:
            if list1[i] <= list2[j]:
                result.append(list1[i])
                i += 1
            else:
                result.append(list2[j])
                j += 1
        if i < length1:
            result.extend(list1[i:])
        if j < length2:
            result.extend(list2[j:])
        return result
        
    def traverse(self, root , arr):
        if root is None:
            return
        self.traverse(root.left, arr)
        if root is not None:
            arr.append(root.val)
        self.traverse(root.right, arr)