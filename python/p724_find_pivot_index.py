from typing import List

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        """
        Create a prefix sum. We have a pivot index when
        left == c_sum - current
        where 
        left = sum[i-1]
        and 
        current = sum[i]
        """
        prefix_sum = []
        c_sum = 0
        for n in nums:
            c_sum += n
            prefix_sum.append(c_sum)
        print(f"PS = {prefix_sum}")
        left = 0
        for i in range(len(prefix_sum)):
            print(f"i = {i}, left = {prefix_sum[i-1]}, right = {c_sum - prefix_sum[i]}")
            if left == c_sum - prefix_sum[i]:
                return i
            left = prefix_sum[i]

        return -1
