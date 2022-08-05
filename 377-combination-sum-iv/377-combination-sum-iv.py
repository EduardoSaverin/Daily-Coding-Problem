class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        nums.sort()
        d = {}
        count = 0
        def recursion(target):
            nonlocal count
            if target == 0:
                return 1
            if target < 0:
                return 0
            if target in d:
                return d[target]
            temp = 0
            for num in nums:
                if target >= num:
                    temp += recursion(target-num)
                else:
                    break
            d[target] = temp
            return d[target]
        recursion(target)
        return d[target]