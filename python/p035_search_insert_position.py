from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        """ Find index of target in list. 
            Split list in half recursively until target is found
            or list has length = 1. 
        """

        l = 0
        r = len(nums)-1
        # First check if target is outside of list
        if target < nums[l]:
            return l
        if target > nums[r]:
            return r+1
        # Compare with middle value and split up list
        index = self.check_middle(l,r,nums,target)
        return index

    def check_middle(self,l,r,nums,target):
        """ Find middle index between left and right. 
            If match then return index. Else search in left half or right half.
        """       
        middle = int((l + r) / 2)
        middle_val = nums[middle]
        if target < nums[l]:
            return l
        elif target > nums[r]:
            return r+1
        elif l==r or middle_val == target:
            return middle
        elif target < middle_val:
            r = middle - 1
        else:
            l = middle + 1

        middle = self.check_middle(l,r,nums,target)
        return middle
