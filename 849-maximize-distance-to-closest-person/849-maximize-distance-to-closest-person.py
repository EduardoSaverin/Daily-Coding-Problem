class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        lastOne = -1
        distance = 0
        for index, seat in enumerate(seats):
            if seat == 1:
                if lastOne == -1:
                    distance = max(distance, index)
                else:
                    distance = max(distance, (index-lastOne)//2)
                lastOne = index
        # For Cases like [1,0,0,0]
        if seats[-1] == 0:
            distance = max(distance, (len(seats) -1 -lastOne))
        return distance
                
        
    def maxDistToClosestOld(self, seats: List[int]) -> int:
        ones = []
        zeros = []
        for index, seat in enumerate(seats):
            if seat == 0:
                zeros.append(index)
            else:
                ones.append(index)
        count = 0
        for zero in zeros:
            distance = float("inf")
            for one in ones:
                distance = min(distance, abs(zero-one))
            count = max(count, distance)
        return count