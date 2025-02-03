from typing import List

class Solution:
    def check(self, nums: List[int]) -> bool:
        """
        Brute force and check if it is possible for a sorted array to start from each position.
        """

        # This method only needs one pass through the array. 
        have_reset = False
        prev = nums[0]
        for num in nums:
            if num < prev:
                if have_reset:
                    return False
                have_reset = True
            prev = num

        if have_reset:
            if nums[len(nums)-1] > nums[0]:
                return False
        return True
            
        # This was my first try, inspired by the hint to use "brute force"
        array_len = len(nums)
        for i in range(array_len):
            valid=True
            for j in range(0,i):
                # check if sorted
                if nums[j] < nums[j-1]:
                    valid=False
                    break
            
            if valid:
                for j in range(i+1, array_len):
                    # check if sorted
                    if nums[j] < nums[j-1]:
                        valid=False
                        break

            if valid:
                return True
      
        return valid