from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        result = [-1,-1]
        if len(nums) < 1 or target < nums[0] or target > nums[len(nums)-1]:
            return result

        count = 0
        found_target = False
        # Could change to binary search - see problem 035. 
        for x in nums:
            if x == target:
                if not found_target:
                    result[0] = count
                    result[1] = count
                    found_target = True
                else:
                    result[1] = count
            count += 1
            if x > target:
                return result
        return result
