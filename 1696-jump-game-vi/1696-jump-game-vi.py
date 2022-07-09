class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        #.
        dq = deque([0])
        for i in range(1, len(nums)):
            # Remove old indexes
            while dq and dq[0] < (i-k):
                dq.popleft()
            # Notice that Line 10 causes dq to be in decreasing order,
            # So [0] element in dq will be max
            nums[i] += nums[dq[0]]
            # Make dq in decreasing order
            while dq and nums[dq[-1]] <= nums[i]:
                dq.pop()
            dq.append(i)
        return nums[-1]
            
            
            