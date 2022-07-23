class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        # Here we are using a simple idea that when we insert element in sorted array index at which position element gets inserted will tell then number of elements which are greater or less than current number.
        sorted_arr = []
        result = []
        for num in nums[::-1]:
            index = bisect_left(sorted_arr, num)
            result.append(index)
            sorted_arr.insert(index, num)
        return result[::-1]
        