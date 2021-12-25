class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort() # For Early Exit
        arr = [0]*(target+1)
        for num in nums:
            if num <= target:
                arr[num] = 1
        for i in range(target+1):
            for num in nums:
                if i-num > 0:
                    arr[i] += arr[i-num]
                else:
                    break
        return arr[-1]