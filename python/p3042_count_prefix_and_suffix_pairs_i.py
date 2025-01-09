from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        n_words = len(words)
        pairs = []
        for i in range(n_words-1):
            str1 = words[i]
            for j in range(i+1,n_words):
                str2 = words[j]
                if (str2.startswith(str1) and str2.endswith(str1)):
                    pairs.append([i,j])
        return len(pairs)

