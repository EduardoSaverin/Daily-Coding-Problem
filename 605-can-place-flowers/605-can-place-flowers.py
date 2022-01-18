class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        for index, val in enumerate(flowerbed):
            if not val and (index == 0 or flowerbed[index-1] == 0) and (index == len(flowerbed)-1 or flowerbed[index+1] == 0):
                n -= 1
                flowerbed[index] = 1
        return n <= 0
                    