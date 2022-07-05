class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        heapq.heapify(nums)
        prev = None
        max_length = 0
        length = 0
        while len(nums):
            num = heappop(nums)
            # print(prev, num)
            if prev is None:
                length += 1
            elif prev == num:
                continue
            elif prev+1 != num:
                max_length = max(max_length, length)
                length = 1
            else:
                length += 1
            prev = num
        max_length = max(length, max_length)
        return max_length