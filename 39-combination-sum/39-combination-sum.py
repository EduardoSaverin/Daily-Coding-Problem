class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        def recursion(candidates, start, total, path, result):
            if total == target:
                result.append(path[:])
                return
            for index in range(start, len(candidates)):
                new_sum = total + candidates[index]
                if new_sum > target:
                    break
                path.append(candidates[index])
                recursion(candidates, index, new_sum, path, result)
                path.pop()
        recursion(candidates, 0, 0, [], result)
        return result