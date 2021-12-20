class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        diff = 10000000
        result = []
        for index in range(1, len(arr)):
            if abs(arr[index] - arr[index-1]) < diff:
                diff = abs(arr[index] - arr[index-1])
        
        for index in range(1, len(arr)):
            if abs(arr[index] - arr[index-1]) == diff:
                result.append([arr[index-1], arr[index]])
        return result