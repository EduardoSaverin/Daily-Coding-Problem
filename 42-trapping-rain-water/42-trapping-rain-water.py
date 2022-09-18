class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        leftmax, rightmax = 0,0
        water = 0
        while left <= right:
            if leftmax <= rightmax:
                if leftmax < height[left]:
                    leftmax = height[left]
                else:
                    water += (leftmax - height[left])
                left += 1
            else:
                if rightmax < height[right]:
                    rightmax = height[right]
                else:
                    water += (rightmax - height[right])
                right -= 1
        return water