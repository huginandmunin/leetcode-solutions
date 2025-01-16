from collections import Counter

class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        if len(s) < k:
            return False

        counts = Counter(list(s))
        n_odd_numbers = 0
        # get number of letters with odd count
        for val in counts.values():
            if val % 2 == 1:
                n_odd_numbers += 1
                if n_odd_numbers > k:
                    return False       
        return True