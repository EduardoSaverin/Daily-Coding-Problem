class NumArray:

    def __init__(self, nums: List[int]):
        self.total = sum(nums)
        self.nums = nums
        self.length = len(nums)
        

    def update(self, index: int, val: int) -> None:
        self.total -= self.nums[index]
        self.nums[index] = val
        self.total += self.nums[index]
        

    def sumRange(self, left: int, right: int) -> int:
        if (right-left) > self.length // 2:
            t = sum(self.nums[:left]) + sum(self.nums[right+1:])
            return self.total - t
        else:
            return sum(self.nums[left:right+1])
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(index,val)
# param_2 = obj.sumRange(left,right)
