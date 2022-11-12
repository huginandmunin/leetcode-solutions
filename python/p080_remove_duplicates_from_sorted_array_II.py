from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) in [0,1,2]:
            return len(nums)

        prev = nums[1]
        prevprev = nums[0]
        # slow pointer for the non-duplicate values
        k = 2

        for i in range(2,len(nums)):
            if ( (nums[i] > prev) or
                 (nums[i]==prev and nums[i] > prevprev) ):
                # shift the current value to the index of the slow pointer
                nums[k] = nums[i]
                # advance the slow pointer
                k += 1
                prevprev = prev
                
            else:
                # this is a duplicate, shift the current value
                nums[i-1] = nums[i]
            prev = nums[i]

        return k

