from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        """
        Use list comprehension to construct a boolean list
        """
        max_candies = max(candies)
        return [x+extraCandies>=max_candies for x in candies]