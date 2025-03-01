from typing import List

class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        """Would be better to swap elements in original array"""

        sorted_nums = []

        for num in nums:
            if num % 2 == 1:
                sorted_nums.append(num)
            else:
                sorted_nums = [num] + sorted_nums

        return sorted_nums