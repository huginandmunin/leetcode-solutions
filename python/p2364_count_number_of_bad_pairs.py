from typing import List

class Solution:
    def countBadPairs(self, nums: List[int]) -> int:

        len_nums = len(nums)
        total_possible_pairs = int(len_nums * (len_nums-1) / 2)
        count_good_pairs = 0
        counter_num_i = {}
        set_num_i = set()

        # get frequency for each value of nums[i]-i
        for i in range(len(nums)):
            num_i = nums[i] - i
            if num_i in set_num_i:
                counter_num_i[num_i] += 1
            else:
                counter_num_i[num_i] = 1
                set_num_i.add(num_i)

        for val in counter_num_i.values():
            # get number of combinations for each set of repeated values
            # and add to count of good pairs
            if val > 1:
                count_good_pairs += int(val * (val-1)/ 2)

        return total_possible_pairs - count_good_pairs

