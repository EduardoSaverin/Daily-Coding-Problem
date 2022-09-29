class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        counter = collections.Counter(changed)
        # Odd Zeroes
        if counter[0] % 2:
            return []
        for ele in sorted(counter):
            if counter[ele] > counter[ele*2]:
                return []
            counter[ele*2] -= counter[ele] if ele else counter[ele]//2
        return list(counter.elements())
                