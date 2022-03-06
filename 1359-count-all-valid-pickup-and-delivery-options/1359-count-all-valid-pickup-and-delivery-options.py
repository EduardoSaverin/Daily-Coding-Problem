class Solution:
    def countOrders(self, n: int) -> int:
        MOD = 10**9+7
        pickup_pos = math.factorial(n) % MOD
        delivery_pos = 1
        for i in range(1, n+1):
            delivery_pos *= (2*i-1)
        return pickup_pos*delivery_pos % MOD