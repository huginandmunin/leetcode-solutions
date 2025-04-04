from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """Use binary search"""

        if target not in nums:
            return -1
        
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (high + low) // 2
            if target == nums[mid]:
                return mid
            if target > nums[mid]:
                low = mid + 1
            else:
                high = mid - 1

        return -1
    
