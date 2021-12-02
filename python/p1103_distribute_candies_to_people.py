from typing import List

class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:

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
