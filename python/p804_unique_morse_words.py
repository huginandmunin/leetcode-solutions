from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        """
        Given an array of strings words where each word can be written 
        as a concatenation of the Morse code of each letter.

        For example, "cab" can be written as "-.-..--...", which is 
        the concatenation of "-.-.", ".-", and "-...". We will call 
        such a concatenation the transformation of a word.

        Return the number of different transformations among 
        all words we have.
        """
        # Store the unique transformed words in a set.
        # Might go faster to store output in list, then convert list to set at the very end. 
        transformed_words = set()
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        for word in words:
            transformed_words.add(''.join([morse[ord(x)-ord('a')] for x in word]))
        return len(transformed_words)
        