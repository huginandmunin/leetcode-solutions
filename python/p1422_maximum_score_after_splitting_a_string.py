from collections import Counter


class Solution:
    def maxScore(self, s: str) -> int:
        """Iterate over chars and keep running count."""        
        max_score = 0       
        count_left = 0
        count_right = Counter(s)["1"]
        # iterate over all chars except last
        for c in s[:-1]:
            if c == "0":
                count_left += 1
            else:
                count_right -= 1
            max_score = max(max_score, count_left + count_right)

        return max_score
            