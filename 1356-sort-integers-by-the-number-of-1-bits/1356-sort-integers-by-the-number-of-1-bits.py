class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        # Pass through array and get number of 1's bits in each number
        # Store this in dict and sort using `value`
        d = []
        for num in arr:
            d.append([num, self.countBits(num)])
        def sort(item1, item2):
            if item1[1] < item2[1]:
                return -1
            elif item1[1] > item2[1]:
                return 1
            else:
                if item1[0] < item2[0]:
                    return -1
                else:
                    return 1
        d = sorted(d, key=functools.cmp_to_key(sort))
        return map(lambda item: item[0],d )
        
    def countBits(self, num: int) -> int:
        count = 0
        while num:
            count += 1 & num
            num = num >> 1
        return count