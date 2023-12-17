from collections import Counter

class Solution:
    def isItPossible(self, word1: str, word2: str) -> bool:
        """Brute force run through all possible 1-character swaps,
           checking if changed words have same number of distinct characters."""
       
        cd1 = Counter(word1)
        chars1 = set(cd1)
        n1 = len(chars1)
        chars_tried1 = []

        cd2 = Counter(word2)
        chars2 = set(cd2)
        n2 = len(chars2)

        for c1 in word1:
            # Only do chars that haven't been swapped out before
            if c1 in chars_tried1:
                continue
            else:
                chars_tried1.append(c1)

            nw2 = ""
            chars_tried2 = [] 
            for c2 in word2:
                if c2 in chars_tried2:
                    continue
                else:
                    chars_tried2.append(c2)

                # check how count changes with swapping of chars
                new_n1 = n1
                new_n2 = n2
                if c1 != c2:
                    if c2 not in chars1:
                        new_n1 = new_n1 + 1
                    if cd1[c1]==1:
                        new_n1 = new_n1 - 1

                    if c1 not in chars2:
                        new_n2 = new_n2 + 1
                    if cd2[c2]==1:
                        new_n2 = new_n2 - 1
                if new_n1 == new_n2:
                    return True
                
            # chars2.append(c2)

        return False
    

    def num_chars(self, word: str):
        return len(set(Counter(word).keys()))
