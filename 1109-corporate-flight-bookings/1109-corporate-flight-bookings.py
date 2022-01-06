class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        l = [0]*(n+1)
        for first, last, seats in bookings:
            l[first-1] += seats
            l[last] -= seats
        for index in range(1, n):
            l[index] += l[index-1]
        return l[:n]