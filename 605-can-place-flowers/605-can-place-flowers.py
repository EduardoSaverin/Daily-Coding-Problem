class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        self.flowerbed = flowerbed
        for index in range(len(flowerbed)):
            if n == 0 :
                return True
            if self.flowerbed[index] == 0 and self.isValid(index):
                self.flowerbed[index] = 1
                n -= 1
        return True if not n else False
    
    def isValid(self, index):
        length = len(self.flowerbed)
        if (index-1) >= 0 and (index+1) < length:
            if self.flowerbed[index-1] != 1 and self.flowerbed[index+1]!=1:
                return True
            else:
                return False
        elif (index-1) >= 0:
            if self.flowerbed[index-1] != 1:
                return True
            else:
                return False
        elif (index+1) < length:
            if self.flowerbed[index+1]!=1:
                return True
            else:
                return False
        elif index == (length-1):
            return True
                    