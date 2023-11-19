from typing import List

class Solution:
    def applyOperations(self, nums: List[int]) -> List[int]:
        # apply first pass operations
        for i in range(len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] *= 2
                nums[i+1] = 0
        # shift zeros to end
        for num in nums:
            if num == 0:
                nums.remove(num)
                nums.append(num)
        return nums
