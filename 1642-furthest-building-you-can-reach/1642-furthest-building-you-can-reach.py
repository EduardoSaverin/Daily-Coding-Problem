class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr = []
        for index in range(len(heights)-1):
            # Find Diff Between Two Adj Building
            diff = heights[index+1] - heights[index]
            # If Diff is greater than 0, means we should climb,
            # First we will use ladder
            if diff > 0:
                heapq.heappush(arr, diff)
            # If Ladders are exhausted, then remove bricks equal to shortest height that ladder climbs
            if len(arr) > ladders:
                bricks -= heapq.heappop(arr)
            # if bricks exhausted then this is farthest index
            if bricks < 0:
                return index
        # Default Condition
        return len(heights)-1