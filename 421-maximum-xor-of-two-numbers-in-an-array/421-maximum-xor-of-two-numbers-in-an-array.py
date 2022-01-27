class Trie():
    def __init__(self):
        self.one = None
        self.zero = None
        self.value = None
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        root = Trie()
        for num in nums:
            node = root
            for i in range(32,-1,-1):
                mask = 1 << i # 00000100000000 1 at ith Position
                masked = num & mask
                if masked is 0:
                    if node.zero is None:
                        node.zero = Trie()
                    node = node.zero
                else:
                    if node.one is None:
                        node.one = Trie()
                    node = node.one
            node.value = num
        
        max_xor = 0
        for num in nums:
            node = root
            for i in range(32,-1,-1):
                mask = 1 << i
                masked  = num & mask
                if masked is 0:
                    if node.one:
                        node = node.one
                    else:
                        node = node.zero
                else:
                    if node.zero:
                        node = node.zero
                    else:
                        node = node.one
            max_for_num = num ^ node.value
            max_xor = max(max_xor, max_for_num)
        return max_xor