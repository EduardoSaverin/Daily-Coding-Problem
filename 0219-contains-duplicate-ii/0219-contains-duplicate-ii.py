class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        for index,val in enumerate(nums):
            d[val].append(index)
        for key, l in d.items():
            if len(l) == 1:
                continue
            for i in range(1, len(l)):
                if abs(l[i] - l[i-1]) <= k:
                    return True
        return False