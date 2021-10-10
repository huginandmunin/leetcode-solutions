from typing import List, Optional

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums)==0:
            return 0
        new_i = 0
        for i in range(len(nums)):
            if nums[i] != val:
                if i > new_i:
                    nums[new_i] = nums[i]
                new_i += 1
        return new_i
