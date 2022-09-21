class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans, curr = [], sum(n for n in nums if n % 2 == 0)
        for val, index in queries:
            prev = nums[index]
            nums[index] += val
            if prev % 2 == 0:
                curr -= prev
            if nums[index] % 2 == 0:
                curr += nums[index]
            ans.append(curr)
        return ans