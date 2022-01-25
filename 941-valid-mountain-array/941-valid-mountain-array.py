class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        left = 0
        while left < len(arr)-1 and arr[left] < arr[left+1]:
            left += 1
        right = len(arr)- 1
        while right >= 1 and arr[right] < arr[right-1]:
            if right < left:
                return False
            right -= 1
        if left == right == 0 or (left == right == len(arr)-1):
            return False
        return left == right