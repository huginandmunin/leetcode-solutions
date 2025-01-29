from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        nums_set = set()
        for num in nums:
            nums_set.add(num)

        prev = 0
        for num in nums_set:
            print(f"num = {num}, prev = {prev}, diff = {num - prev}")
            if num - prev > 1:
                return num - 1
            prev = num
            
        # chck for missing 0 or n
        n = len(nums)
        if n not in nums_set:
            return n
        if 0 not in nums_set:
            return 0
