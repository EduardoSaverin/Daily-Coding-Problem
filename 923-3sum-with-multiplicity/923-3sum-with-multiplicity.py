class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        result = 0
        MOD = 10**9+7
        d = defaultdict(int)
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                remainder = target - arr[i] - arr[j]
                # If `remainder` is in dict then simply get its count,
                # Because that will be the number of way this total sum can be acheived
                if remainder in d:
                    result += d[remainder]
            # Simply Counting Seen Elements so far
            d[arr[i]] += 1
        return result % MOD