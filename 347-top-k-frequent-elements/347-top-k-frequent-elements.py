class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        arr = []
        counter = Counter(nums)
        d = dict(counter)
        for key, value in d.items():
            heapq.heappush(arr, (-value, key))
        result = []
        while k:
            _, key = heapq.heappop(arr)
            result.append(key)
            k -= 1
        return result