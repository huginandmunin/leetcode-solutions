from typing import List

class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        """
        Iterate over elements in list. Form an item
        by removing an element from the list and recursively
        call the function on the remainder of the list.
        """
        if len(nums)<=1:
            return [nums]
        result = []
        for i in range(len(nums)):
            item = nums[i]
            for p in self.permute(nums[:i] + nums[i+1:]):
                result.append([item] + p)
    
        return result

