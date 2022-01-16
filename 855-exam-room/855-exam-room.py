class ExamRoom:

    def __init__(self, n: int):
        self.total = n
        self.arr = []

    def seat(self) -> int:
        if not self.arr:
            self.arr.append(0)
            return 0
        previous, distance, seat = -1, self.arr[0], 0
        for seating in self.arr:
            if previous > -1:
                d = (seating - previous)//2
                if d > distance:
                    distance = d
                    seat = previous + d
            previous = seating
        if (self.total -1 - self.arr[-1]) > distance:
            seat = self.total - 1
        index = 0
        while index < len(self.arr) and self.arr[index] < seat:
            index += 1
        self.arr.append(seat)
        self.arr.sort()
        return seat
    
    def leave(self, p: int) -> None:
        self.arr.remove(p)
        


# Your ExamRoom object will be instantiated and called as such:
# obj = ExamRoom(n)
# param_1 = obj.seat()
# obj.leave(p)