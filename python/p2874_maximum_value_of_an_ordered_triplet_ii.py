from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        "The hints suggest using prefix and suffix arrays"

        nums_len = len(nums)
        max_triplet_value = 0

        # prefix and suffix array
        prefix_max = [0] * nums_len
        max_num_i = nums[0]
        for i in range(nums_len):
            max_num_i = max(max_num_i, nums[i])
            prefix_max[i] = max_num_i

        suffix_max = [0] * nums_len
        max_num_i = nums[-1]
        for i in range(nums_len-1, -1, -1):
            max_num_i = max(max_num_i, nums[i])
            suffix_max[i] = max_num_i

        # hint 3, use the arrays to get maximum
        for j in range(1, nums_len - 1):
            triplet_value = (prefix_max[j-1] - nums[j]) * suffix_max[j + 1]
            max_triplet_value = max(max_triplet_value, triplet_value)

        return max_triplet_value