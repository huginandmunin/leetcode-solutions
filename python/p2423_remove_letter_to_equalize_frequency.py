from collections import Counter

class Solution:
    def equalFrequency(self, word: str) -> bool:
        """Get counts with Counter, form set of counts values"""
        counts = Counter(word)
        keys = list(counts.keys())
        for c in keys:
            cd = dict(counts)
            cd[c] = cd[c] - 1
            s = set(cd.values())
            s.discard(0)
            if len(s)==1:
                return True
        return False
