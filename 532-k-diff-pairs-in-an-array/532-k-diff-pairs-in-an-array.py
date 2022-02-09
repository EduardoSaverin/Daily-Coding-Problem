from collections import defaultdict
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        result = set()
        d = self.get_hashmap(nums)
        for num in nums:
            diff = num-k
            if diff in d:
                if (diff == num and d[diff] > 1) or diff != num:
                    result.add((diff,num) if diff < num else (num, diff))
        return len(result)
        
    def get_hashmap(self, nums):
        d = defaultdict(int)
        for num in nums:
            d[num] += 1
        return d