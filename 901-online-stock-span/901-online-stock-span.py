class StockSpanner:

    def __init__(self):
        # [price, totalSpan]
        self.stack = []

    def next(self, price: int) -> int:
        totalSpan = 1
        while self.stack and self.stack[-1][0] <= price:
            totalSpan += self.stack.pop()[1]
        self.stack.append([price, totalSpan])
        return totalSpan
        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)