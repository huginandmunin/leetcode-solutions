from typing import List
from collections import Counter

class Solution:
    def areOccurrencesEqual(self, s: str) -> bool:
        """
        Use collections.Counter to get a dictionary of counts per character.
        Cast the counts into a set. The set would have a length of 1 if all counts are the same.
        """
        return len(set(Counter(s).values()))==1
