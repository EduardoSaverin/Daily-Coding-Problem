from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        # n^4 when doing burte force so lets break that into n^2 + n^2 :D
        d = defaultdict(int)
        for i in nums3:
            for j in nums4:
                d[i+j] += 1
        print(d)
        count = 0
        for value in nums1:
            for val in nums2:
                temp = -(value+val)
                if temp in d and d[temp] != 0:
                    count += d[temp]
        return count
                