class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def recursion(nums, start, path, result):
            result.append(path[:])
            for index in range(start, len(nums)):
                # Eliminate the dup with sort and then the condition: do not put this element inside, if it has same element before && the former dup has not been put into it. 
                if index != start and nums[index] == nums[index-1]:
                    continue
                path.append(nums[index])
                # print(path)
                recursion(nums, index+1, path, result)
                path.pop()
        result = []
        recursion(nums, 0, [], result)
        return result