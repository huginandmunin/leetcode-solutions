from typing import List

class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> bool:

        # This method only needs one pass through the array.
        prev = nums.pop(0)
        count_inc = 1
        count_dec = 1
        max_inc = 0
        max_dec = 0
        for num in nums:
            if num < prev:
                # increment decreasing, save max number increasing, reset increasing,
                count_dec += 1
                max_inc = max(max_inc, count_inc)
                count_inc = 1
            elif num > prev:
                # increment increasing, save max number decreasing, reset decreasing
                count_inc += 1
                max_dec = max(max_dec, count_dec)
                count_dec = 1
            elif num == prev:
                # save max number increasing and decreasing, reset
                max_inc = max(max_inc, count_inc)
                max_dec = max(max_dec, count_dec)
                count_inc = 1
                count_dec = 1
            prev = num     

        # check for max again in case there were any more increments
        max_inc = max(max_inc, count_inc)
        max_dec = max(max_dec, count_dec)
        print(f"Max inc = {max_inc}, Max dec = {max_dec}")
        return max(max_inc, max_dec)
            
