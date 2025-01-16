from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        Solution Hint: Find the highest possible frequencies of each character
        appearing in any string in words2, then check which strings in words1
        satisfy these frequencies!
        """

        result = []

        words1_counts = {}
        for word in words1:
            word_list = list(word)
            counts = Counter(word_list)
            words1_counts[word] = counts

        # print(f"Words1_count {words1_count}")

        # change this to a max count of all words in words2 - just one dict.,
        # eg {"l": 1, "e": 1}
        words2_count = {}
        for word in words2:
            word_list = list(word)
            counts = Counter(word_list)
            print(f"Counts = {counts}")
            for key, val in counts.items():
                print(f"key={key}, val={val}")
                if key in words2_count.keys():
                    words2_count[key] = max(val, words2_count[key])
                else:
                    print(f"setting key {key} to val {val}")
                    words2_count[key] = val

        print(f"Words2_count {words2_count}")

        for word, word_count in words1_counts.items():
            # check if all strings in b are a subset of word
            # print(f"Ready to check word {word}")
            if self.is_universal(word_count,words2_count):
                   result.append(word)
        return result


    def is_universal(self,word_count,words2_count):
        for key, val in words2_count.items():
            print(f"key={key}, val={val}")
            print(f"word keys {list(word_count.keys())}")
            print(f"word val {word_count.get(key)}")
            if key not in list(word_count.keys()):
                print(f"{key} not in word")
                return False
            elif val > int(word_count[key]):
                print(f"Val is {val}, but only {word_count[key]} in word")
                return False
        return True