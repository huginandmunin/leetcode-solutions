
class Solution:
    def lengthOfLastWord(self, s: str) -> int:

        # Start at tail and count characters until you get to a space
        if len(s) == 1 and s != ' ':
            return 1

        j = len(s) - 1
        count = 0
        in_word = False
        while (j>=0):
            if s[j] != ' ':
                in_word = True
                count += 1
            if in_word and s[j]==' ':
                return count
            j -= 1
        return count
