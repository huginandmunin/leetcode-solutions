from time import time
from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        last = -1

        for t in timeSeries:
            reset = 0
            # check if we need to reset timer
            if t <= last:
                reset = last - t + 1

            total += duration - reset
            last = t + duration - 1

        return total


