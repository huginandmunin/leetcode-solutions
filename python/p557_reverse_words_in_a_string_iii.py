class Solution:
    def reverseWords(self, s: str) -> str:

        words = s.split()
        new_words = []
        for word in words:
            wl = list(word)
            wl.reverse()
            new_word = ''.join(wl)
            new_words.append(new_word)

        return ' '.join(new_words)


