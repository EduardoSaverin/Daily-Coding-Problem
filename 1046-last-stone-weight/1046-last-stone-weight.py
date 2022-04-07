class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        arr = []
        for stone in stones:
            heapq.heappush(arr, (-stone, stone))
        while arr:
            if len(arr) == 1:
                _, stone = heapq.heappop(arr)
                return stone
            _, stone1 = heapq.heappop(arr)
            _, stone2 = heapq.heappop(arr)
            if stone1 == stone2:
                pass
            elif stone1 != stone2:
                left = abs(stone1-stone2)
                heapq.heappush(arr, (-left, left))
        return 0