class Solution:
    def minMoves(self, nums: List[int]) -> int:
        nums.sort()
        moves = 0
        for index in range(len(nums)-1, -1, -1):
            if nums[index] == nums[0]:
                break
            moves += (nums[index] - nums[0])
        return moves
    