class Solution:
    def maxLength(self, arr: List[str]) -> int:
        return self.recursive(arr, 0 , '')
    
    def recursive(self, arr, start, path):
        max_length = 0
        for index in range(start, len(arr)):
            if len(path + arr[index]) == len(set(path + arr[index])):
                this_length = len(path+arr[index])
                l = self.recursive(arr, index+1, path + arr[index])
                max_length = max(max_length, l, this_length)
        return max_length