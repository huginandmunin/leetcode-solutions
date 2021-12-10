import collections

class Solution:
    def frequencySort(self, s: str) -> str:
        """
        Given a string s, sort it in decreasing order based on 
        the frequency of the characters. 
        The frequency of a character is the number of times it appears in the string.
        """

        counts_dict = collections.Counter(s)
        sorted_counts = sorted(counts_dict.items(), key=lambda x: (-x[1], x[0]))
        result = ''
        for item in sorted_counts:
            result += item[0]*item[1]
        return result




