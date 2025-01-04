from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:

        vowels = set(['a','e','i','o','u'])
        words_sum = []
        running_sum = 0
        result = []
        for word in words:
            if word[0] in vowels and word[-1] in vowels:
                    running_sum += 1
            words_sum.append(running_sum)

        for r in queries:
            count = words_sum[r[1]]
            if r[0] > 0:
                count -= words_sum[r[0]-1]
            result.append(count)

        return result

