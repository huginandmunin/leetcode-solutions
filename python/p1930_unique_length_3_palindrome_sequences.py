class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:

        palindrome_count = 0
        letter_indexes = {}
        for i in range(len(s)):
            c = s[i]
            if c in letter_indexes.keys():
                letter_indexes[c].append(i)            
            else:
                letter_indexes[c] = [i]

        # look for palindromes
        for key,value in letter_indexes.items():
            if len(value) >= 2:
                # possible palindromes
                palindrome_count += len(set(s[value[0]+1:value[-1]]))

        return palindrome_count