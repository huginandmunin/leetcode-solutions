from typing import List
from collections import Counter

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        """
        Return number of different types from list if selecting n / 2.
        """

        # Get a count of total number of different types available
        # A couple of easy options (but slower) are:
        # n_types = len(Counter(candyType).keys())
        # n_types = len(set(candyType))

        candyType.sort()
        n_types = 0
        prev = candyType[0]-1
        for type in candyType:
            if type > prev:
                n_types += 1
                prev = type

        # Select mininum between total possible and number available
        return min( n_types, len(candyType)//2 )
