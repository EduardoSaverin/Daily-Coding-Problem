"""Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

    Returns:
        [float]: [median of two sorted arrays]
"""
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        median = total // 2
        if len(nums2) < len(nums1):
            nums1, nums2 = nums2, nums1 # Assuming nums1 (A) is always <= other array i.e nums2 (B)
        left, right = 0, len(nums1)-1
        # Complexity : O(log(min(n,m)))
        while True:
            i = (left + right) // 2
            j = median - i -2 # Extra -2 because both array start at 0 index so -1 for both
            # if any index gets out of range use -inf or +inf
            Aleft = nums1[i] if i>=0 else float("-infinity")
            ARight = nums1[i+1] if (i+1) < len(nums1) else float("infinity")
            BLeft = nums2[j] if j>=0 else float("-infinity")
            BRight = nums2[j+1] if (j+1) < len(nums2) else float("infinity")
            if Aleft <= BRight and BLeft <= ARight:
                # Odd Elements
                if total % 2:
                    return min(ARight, BRight)
                # Event elements : get max of left parition , get min of right parition / 2
                return (max(Aleft, BLeft) + min(ARight,BRight))/2
            elif Aleft > BRight:
                # Highest element of A's Left Parition > first element of B's Right Parition
                right = i - 1
            else:
                # Highest element of A's Left Parition < first element of B's Right Parition
                left = i + 1
