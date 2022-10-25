from collections import Counter
from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Get number of 1's per number and add to list
        return [Counter(bin(i))['1'] for i in range(n+1)]
