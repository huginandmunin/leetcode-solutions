from typing import List, Optional

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        new_i = 1
        for i in range(1,len(nums)):
            if nums[i] > nums[i-1]:
                if i > new_i:
                    nums[new_i] = nums[i]
                new_i += 1
        return new_i

