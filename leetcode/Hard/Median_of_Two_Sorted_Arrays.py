"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).



Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

"""

def findMedianSortedArrays( nums1: List[int], nums2: List[int]) -> float:
    nums3 = (nums1 + nums2)
    nums3.sort()
    Len_n3 = len(nums3)
    if Len_n3 % 2 == 0:
        i = int(Len_n3 / 2)
        return (nums3[i] + nums3[i - 1]) / 2
    else:
        return nums3[int(Len_n3 / 2)]
