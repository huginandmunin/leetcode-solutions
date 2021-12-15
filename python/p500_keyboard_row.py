from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        """
        Given an array of strings words, return the words that 
        can be typed using letters of the alphabet on only one 
        row of American keyboard like the image below.
        """

        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        results = []

        # Loop over words
        for word in words:
            # Loop over rows
            for i in range(len(rows)):
                # Use sets to check if characters from word are in this row.
                if len(list(set(word.lower()) - set(rows[i])))==0:
                    results.append(word)
                    # Skip remaining keyboard rows
                    break

        return results
