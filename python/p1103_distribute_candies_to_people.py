from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
        """
        This solution steps through the results array.

        The hints mention adding the whole array until there aren't enough candies.
        You could use the zip function to add [1,2,3,...] to your initial array [0,0,0,...]
        """

        result = [0]*num_people
        give_num = 0
        i = 0
        while candies > 0:
            give_num += 1
            if give_num > candies:
                give_num = candies
            candies -= give_num
            result[i] += give_num
            if i == num_people-1:
                i = 0
            else:
                i+= 1

        return result
