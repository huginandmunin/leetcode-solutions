from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dict = {}
        for n in nums:
            print(f'Checking {n}')
            if n in num_dict.keys():
                num_dict[n] += 1
            else:
                num_dict[n] = 1
            print(f'dict {num_dict}')
        for item in num_dict.items():
            if item[1] >= len(nums)/2:
                return item[0]
        return None
