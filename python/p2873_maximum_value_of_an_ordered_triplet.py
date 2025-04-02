from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        "The hint suggests looping over indexes - very slow, n^3"

        nums_len = len(nums)
        max_triplet_value = 0

        for i in range(nums_len-2):
            for j in range(i+1, nums_len-1):
                for k in range(j+1, nums_len):
                    triplet_value = (nums[i] - nums[j]) * nums[k]
                    max_triplet_value = max(max_triplet_value, triplet_value)

        return max_triplet_value
