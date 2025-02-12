from typing import List

class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        """Get dict of numbers grouped by digit sum"""
        nums_dict = {}
        max_sum = -1 
        for num in nums:
            num_list = list(str(num))
            sum = 0
            for num_str in num_list:
                sum += int(num_str)

            if sum in nums_dict.keys():
                nums_dict[sum].append(num)
            else:
                nums_dict[sum] = [num]

        for key in nums_dict.keys():
            if len(nums_dict[key]) >= 2:
                nums_dict[key].sort()
                max_sum = max(max_sum, nums_dict[key].pop() + nums_dict[key].pop())

        return max_sum

        