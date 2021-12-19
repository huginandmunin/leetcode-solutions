from typing import List

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        """
        Given a binary array nums, return the maximum number of 
        consecutive 1's in the array.
        """
        count = 0
        result = 0
        for num in nums:
            if num == 0:
                result = max(result,count)
                count = 0
            else:
                count += 1
        result = max(result,count)
        return result
