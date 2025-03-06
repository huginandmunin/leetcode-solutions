from typing import List

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:

        twice = None
        missing = None
        nums_list = []

        for row in grid:
            for num in row:
                if num in nums_list:
                    twice = num
                else:
                    nums_list.append(num)

        nums_list = sorted(nums_list)
        print(f"nums_list {nums_list}")

        prev = nums_list[0]
        if prev > 1:
            return [twice, prev - 1]
        
        for num in nums_list:
            if num - prev > 1:
                missing = num - 1
                break
            prev = num

        if missing is None:
            missing = num + 1

        return [twice, missing]
