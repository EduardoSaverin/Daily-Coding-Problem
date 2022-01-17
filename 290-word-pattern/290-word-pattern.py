class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        arr = s.split()
        vals = set()
        if len(pattern) != len(arr):
            return False
        d = {}
        for index in range(len(arr)):
            if pattern[index] in d:
                if d[pattern[index]] != arr[index]:
                    return False
            elif arr[index] in vals:
                return False
            else:
                vals.add(arr[index])
                d[pattern[index]] = arr[index]
        return True