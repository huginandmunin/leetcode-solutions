from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Convert lists to sets and perform bitwise AND"""
        return list(set(nums1) & set(nums2))