from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        splits = 0
        prefix_sum = []
        c_sum = 0

        for n in nums:
            c_sum += n
            prefix_sum.append(c_sum)

        print(f"prefix_sun = {prefix_sum}")
        for i in range(len(nums)-1):
            if prefix_sum[i] >= c_sum / 2:
                splits += 1
                print(f"Split at {i}")

        return splits