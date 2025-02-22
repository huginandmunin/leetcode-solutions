from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        For each element find the highest to left and right.
        Water is trapped when h < min(left,right)
        Ends will be zero.
        """

        max_left = []
        max_right = [0] * len(height)
        total_water = 0

        left = 0
        for h in height:
            if h > left:
                left = h
            max_left.append(left)
        print(f"left is {max_left}")
        
        right = 0
        for i in range(len(height)-1, -1, -1):
            h = height[i]
            if h > right:
                right = h
            max_right[i] = right

        print(f"right is {max_right}")

        for i in range(1, len(height)-1):
            h = height[i]
            min_left_and_right = min(max_left[i], max_right[i])
            print(f"Element has height {h}, min is {min_left_and_right}")
            water = min_left_and_right - h
            if water > 0:
                total_water += water

        return total_water