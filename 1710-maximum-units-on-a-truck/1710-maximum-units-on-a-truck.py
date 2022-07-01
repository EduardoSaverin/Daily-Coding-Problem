class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        # Sorted the boxes with maximum number of units in them
        boxTypes.sort(key=lambda x : -x[1])
        max_units = 0
        index = 0
        while truckSize > 0 and index < len(boxTypes):
            boxes_pick = min(boxTypes[index][0], truckSize)
            max_units += boxTypes[index][1]*boxes_pick
            truckSize -= boxes_pick
            index += 1
        return max_units