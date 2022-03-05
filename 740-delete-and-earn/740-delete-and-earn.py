class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        d = defaultdict(int)
        # Count Number of Occurences
        for num in nums:
            d[num] += 1
        # If Key 2 Appears 2 Times then its total will be simply key*val
        for key,val in d.items():
            d[key] = key*val
        max_val = max(d.keys())
        l = [0]*(max_val+1)
        for index in range(max_val+1):
            if index in d:
                l[index] = d[index]
        return self.houseRobber(l)
        
    def houseRobber(self, nums) -> int:
        if len(nums)==1:
            return nums[0]
        elif len(nums) == 2:
            return max(nums[0], nums[1])
        nums[2] = nums[2] + nums[0]
        for index in range(3, len(nums)):
            nums[index] = nums[index] + max(nums[index-2], nums[index-3])
        return max(nums[len(nums)-1], nums[len(nums)-2])
        
            
                