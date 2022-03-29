class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        counter = Counter(nums)
        for key, count in counter.most_common():
            if count == 1:
                break
            return key
        return -1