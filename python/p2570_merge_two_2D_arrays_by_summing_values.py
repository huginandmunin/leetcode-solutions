from typing import List

class Solution:
    def mergeArrays(
            self, nums1: List[List[int]], nums2: List[List[int]]
    ) -> List[List[int]]:
        """
        This solutions uses a dictionary.
        For larger arrays you could also
        use a two-pointer method.
        """
        
        all_nums = {}
        all_nums = self.add_nums_to_dict(nums1, all_nums)
        all_nums = self.add_nums_to_dict(nums2, all_nums)

        return [[key,all_nums[key]] for key in sorted(all_nums.keys())]


    def add_nums_to_dict(self, nums: List[List[int]], all_nums) -> dict:
        for num in nums:
            if num[0] in all_nums:
                all_nums[num[0]] += num[1]
            else:
                all_nums[num[0]] = num[1]
                
        return all_nums

        