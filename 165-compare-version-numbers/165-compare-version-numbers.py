class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        result = 0
        arr1 = version1.split('.')
        arr2 = version2.split('.')
        length = min(len(arr1), len(arr2))
        index = 0
        while index < length:
            if int(arr1[index]) < int(arr2[index]):
                return -1
            elif int(arr1[index]) > int(arr2[index]):
                return 1
            index += 1
        index1 = index
        index2 = index
        while index1 < len(arr1):
            if int(arr1[index1]) != 0:
                return 1
            index1 += 1
        while index2 < len(arr2):
            if int(arr2[index2]) != 0:
                return -1 
            index2 += 1
        return result