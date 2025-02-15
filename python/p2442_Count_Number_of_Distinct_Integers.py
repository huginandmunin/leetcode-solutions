from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        distinct_set = set()

        for num in nums:
            distinct_set.add(num)
            if num > 9:
                new_num = self.reverse_number(num)
                distinct_set.add(new_num)
                
        return len(distinct_set)  


    def reverse_number(self, num: int) -> int:
        """Reverse the digits in a number"""
        num_list = list(str(num))
        num_list.reverse()
        return int(''.join(num_list))

