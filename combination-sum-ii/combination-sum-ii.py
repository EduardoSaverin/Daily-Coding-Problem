class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result = []
        print(candidates)
        def recursion(candidates, start, path, total, target):
            nonlocal result
            if target == total:
                result.append(path[:])
                return
            for index in range(start, len(candidates)):
                if index > start and candidates[index] == candidates[index-1]:
                    continue
                if total+candidates[index] > target:
                    break
                path.append(candidates[index])
                recursion(candidates,index+1, path, total+candidates[index], target)
                path.pop()
        recursion(candidates,0,[],0, target)
        return result