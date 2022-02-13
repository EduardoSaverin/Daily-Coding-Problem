class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        def recursion(nums, start, path, result):
            result.append(path[:])
            for index in range(start, len(nums)):
                path.append(nums[index])
                recursion(nums, index+1, path, result)
                path.pop()
        recursion(nums,0, [], result)
        return result