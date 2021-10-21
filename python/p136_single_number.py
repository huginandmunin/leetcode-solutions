from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        """ Counts for each number are stored in a dictionary """
        counts_dict = {}

        for n in nums:
            if n in counts_dict.keys():
                counts_dict[n] += 1
            else:
                counts_dict[n] = 1
        for k, v in counts_dict.items():
            if v == 1:
                return k
        