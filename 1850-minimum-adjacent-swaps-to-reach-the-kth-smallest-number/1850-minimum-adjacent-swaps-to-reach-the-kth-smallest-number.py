class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
        list_of_num = list(num)
        for index in range(k):
            self.nextPermutation(list_of_num)
        count = 0
        num = list(num)
        length = len(num)
        return self.numberOfSwaps(list_of_num, num)
    
    def numberOfSwaps(self, list_of_num, num) -> int:
        count = 0
        num = list(num)
        length = len(num)
        # Simply Compairing Number
        for i in range(length):
            j = i
            while j < length and list_of_num[i] != num[j]:
                j += 1
            count += j - i
            num[i:j+1] = [num[j]] + num[i:j]
        return count
    
    # Taken From Problem 31
    def nextPermutation(self, nums: List[int]) -> None:
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