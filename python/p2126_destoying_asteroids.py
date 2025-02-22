from typing import List

class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        """
        Sort the list and run through the list with a cumulative sum.
        If any list[i+1] is greater than sum[i] then return False.
        """

        asteroids.sort()
        cumulative_mass = mass
        for asteroid in asteroids:
            if cumulative_mass < asteroid:
                return False
            cumulative_mass += asteroid

        return True
