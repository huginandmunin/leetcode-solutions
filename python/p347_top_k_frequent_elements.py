from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """ Given an integer array nums and an integer k, 
            return the k most frequent elements. You may return the answer in any order.
        """
        int_list=[]
        counts = {}
        # this block could be replaced by collections.Counter(nums) 
        for i in nums:
            if i in counts.keys():
                counts[i] += 1
            else:
                counts[i] = 1
        # Sort by vals
        counts_list = sorted(counts.items(), key=lambda item:item[1], reverse=True)
        # Grab the first k keys
        int_list = [c[0] for c in counts_list][0:k]

        return int_list

