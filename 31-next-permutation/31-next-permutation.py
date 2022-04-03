class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        # Approach
        # 1. From end find first index where index-1 < index. It means all elements after index are decreasing.
        # 2. You can think of above sequence that we try to find out is [3,2,1]
        # 3. If index == 0 it means it is something like [3,2,1], so only permumation is to reverse org. array
        # 4. If not equal to 0 , then find first number greater than (index-1)
        # 5. Swap the two, then reverse whole sub-array arr[index:]
        i = j = len(nums)-1
        while i > 0 and nums[i-1] >= nums[i]:
            i -= 1
        if i == 0:
            nums.reverse()
            return
        while nums[j] <= nums[i-1]:
            j -= 1
        nums[i-1] , nums[j] = nums[j], nums[i-1]
        left = i
        right = len(nums)-1
        while left < right:
            nums[left], nums[right] = nums[right] , nums[left]
            left += 1
            right -= 1
            
        