from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
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
            for p in self.permuteUnique(nums[:i] + nums[i+1:]):
                new_item = [item] + p
                if new_item not in result:
                    result.append(new_item)
    
        return result

