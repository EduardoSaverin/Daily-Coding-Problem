class Solution:
    def rangeBitwiseAnd(self, left: int, right: int) -> int:
        # Totally Math logic 
        # https://www.youtube.com/watch?v=-qrpJykY2gE&ab_channel=TECHDOSE
        s = 0
        while left != right:
            left = left >> 1
            right = right >> 1
            s += 1
        return left << s