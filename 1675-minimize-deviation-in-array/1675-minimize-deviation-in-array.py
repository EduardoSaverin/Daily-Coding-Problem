class Solution:
    def minimumDeviation(self, nums: List[int]) -> int:
        heap = []
        minimum  = float("inf")
        for num in nums:
            if num % 2 == 1:
                heap.append(-num*2) # Make all odds as even
            else:
                heap.append(-num) # Keep even same
        minimum = -max(heap) # Pick Minimum from list
        # print('Minimum', minimum)
        heapq.heapify(heap)
        diff = float("inf")
        while True:
            ele = -heapq.heappop(heap) # Get max element from heap
            diff = min(diff, ele - minimum) # Get Difference b/w min and max
            # print('Element', ele)
            if ele & 1: # If Max is odd then simply return
                return diff
            ele >>= 1 # Divide by half
            minimum = min(minimum, ele) # Get new minimum
            heapq.heappush(heap, -ele) # Put half of max back to heap
        return diff