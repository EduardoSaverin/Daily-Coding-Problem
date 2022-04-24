class UndergroundSystem:

    def __init__(self):
        self.in_transit = {}
        self.db = {}
        

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.in_transit[id] = [stationName, t]
        

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        startStationName, startTime = self.in_transit[id]
        totalTime = t - startTime
        key = startStationName + ":" + stationName
        if key in self.db:
            time, trips = self.db[key]
            new_time = (time + totalTime)
            self.db[key] = [new_time, trips+1]
        else:
            self.db[key] = [totalTime, 1]

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = startStation + ":" + endStation
        time, trips = self.db[key]
        return time / trips


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)