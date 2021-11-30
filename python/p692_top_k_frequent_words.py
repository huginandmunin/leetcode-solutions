from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """
        Use collections.Counter to get a dictionary of words and counts.
        Sort the the dictionary by descending counts, ascending words.
        Return the first k keys from the sorted counts.
        """
        counts = Counter(words)
        sorted_counts = sorted(counts.items(), key=lambda x: (-x[1], x[0]))
        sorted_words = [x[0] for x in sorted_counts][0:k]
        return sorted_words