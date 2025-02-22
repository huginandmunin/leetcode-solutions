from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        """Time limit exceeded for large array"""

        # A naive approach gives a time-limit-exceeded error
        # for a large array
        # while len(nums) > 0:
        #     test_num = nums.pop(0)
        #     if test_num in nums:
        #         return True
        # return False

        # Usually, problems of uniqueness can be handled with a set
        if len(nums) != len(set(nums)):
            return True
        else:
            return False

