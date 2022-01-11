class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        # Got this formula using equations 4*x+2*y = tomatoSlices , x+y=cheeseSlices
        y = (2*cheeseSlices - tomatoSlices/2)
        x = (cheeseSlices-y)
        if x < 0 or y < 0 or x%1 or y%1:
            return []
        return [int(x),int(y)]
    
    # TLE with test case 1000000 1000000
    def numOfBurgersOld(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        @lru_cache()
        def recursion(tomatoSlices, cheeseSlices, jumbo, small):
            if tomatoSlices  == 0 and cheeseSlices == 0:
                return [jumbo, small]
            elif tomatoSlices  < 0 or cheeseSlices < 0:
                # print(jumbo, small)
                return []
            r1 = recursion(tomatoSlices-4, cheeseSlices-1, jumbo + 1, small)
            if r1 :
                return r1
            r2 = recursion(tomatoSlices-2, cheeseSlices-1, jumbo, small+1)
            return r2
        result = recursion(tomatoSlices, cheeseSlices, 0, 0)
        return result