class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        result = 0
        while left < right:
            result = max(result, min(height[right], height[left])*(right-left))
            if height[right] < height[left]:
                right -= 1
            else:
                left += 1
        return result
            