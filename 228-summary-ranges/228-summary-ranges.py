class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        if not nums:
            return []
        left = right = None
        result = []
        for num in nums:
            if left is None:
                left = right = num
                continue
            if (num-right) == 1:
                right = num
            elif num - left > 1:
                if left == right:
                    result.append(f"{left}")
                else:
                    result.append(f"{left}->{right}")
                left = right = num
        if left == right:
            result.append(f"{left}")
        else:
            result.append(f"{left}->{right}")
        return result