from typing import List

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """Use a naive approach of iterating through the lists"""
        result = []

        for n1 in nums1:
            if n1 in nums2:
                result.append(n1)
                nums2.remove(n1)
        return result