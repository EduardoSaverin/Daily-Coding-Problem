class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        l = []
        for trip in trips:
            l.append((trip[1], trip[0]))
            l.append((trip[2], -trip[0]))
        l.sort()
        passenger_in_car = 0
        for point, num in l:
            passenger_in_car += num
            if passenger_in_car > capacity:
                return False
        return True