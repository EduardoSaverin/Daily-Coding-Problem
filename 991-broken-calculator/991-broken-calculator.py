class Solution:
    def brokenCalc(self, startValue: int, target: int) -> int:
        # Instead of subtract and multiply do add and divide.
        # For Division we need to have even 
        operations = 0
        while target > startValue:
            operations += 1
            if target % 2 == 1:
                target += 1
            else:
                target = target // 2
        return operations + (startValue-target)