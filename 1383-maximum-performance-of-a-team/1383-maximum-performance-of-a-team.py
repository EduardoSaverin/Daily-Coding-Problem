class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        arr = []
        result = 0
        speed_sum = 0
        for e, s in sorted(zip(efficiency, speed), reverse=1):
            heapq.heappush(arr, s)
            speed_sum += s
            if len(arr) > k:
                speed_sum -= heapq.heappop(arr)
            result = max(result, speed_sum*e)
        return result % (10**9+7)