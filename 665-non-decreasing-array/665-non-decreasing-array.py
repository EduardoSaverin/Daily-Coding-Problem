class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        spikes = 0
        for index in range(1, len(nums)):
            if nums[index-1] > nums[index]:
                spikes += 1
                # If this is 2nd index or value at 2-back index is also less than this current index
                if (index-2) < 0 or nums[index-2] <= nums[index]:
                    nums[index-1] = nums[index]
                else:
                    nums[index] = nums[index-1]
        return spikes <= 1