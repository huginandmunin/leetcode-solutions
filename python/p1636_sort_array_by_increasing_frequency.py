import collections
from typing import List

class Solution:
    def frequencySort(self, nums: List[int]) -> str:
        """
        Given an array of integers nums, sort the array 
        in increasing order based on the frequency of the values. 
        If multiple values have the same frequency, 
        sort them in decreasing order.
        """

        # Create a dictionary of counts per digit
        counts_dict = collections.Counter(nums)
        # Sort the dictionary by increasing counts and decreasing order
        sorted_counts = sorted(counts_dict.items(), key=lambda x: (x[1], -x[0]))
        # Create an output list
        result = []
        for item in sorted_counts:
            result += [item[0]]*item[1]
        return result