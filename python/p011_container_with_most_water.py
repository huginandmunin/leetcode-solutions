from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Hint #2:Try to use two-pointers. Set one pointer to
        the left and one to the right of the array.
        Always move the pointer that points to the lower line.
        """

        most_water = 0
        left = 0
        right = len(height) - 1

        while left <= right:
            # get water for these heights
            h = min(height[left], height[right])
            water = h * (right - left)

            if water > most_water:
                most_water = water

            # move a pointer
            if height[right] > height[left]:
                left += 1
            else:
                right -= 1

        return most_water