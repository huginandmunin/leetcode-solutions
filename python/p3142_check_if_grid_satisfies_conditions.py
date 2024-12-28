from typing import List

class Solution:
    def satisfiesConditions(self, grid: List[List[int]]) -> bool:

        prev_item = None
        for item in grid[0]:
            if item == prev_item:
                return False
            prev_item = item

        prev_row = grid[0]
        for row in grid:
            if row != prev_row:
                return False
            prev_row = row

        return True