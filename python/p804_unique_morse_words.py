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
        # Store the transformed words in a list then get uniqueness by 
        # converting to set.
        transformed_words = []
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---",
                 "-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-",
                 "...-",".--","-..-","-.--","--.."]
        for word in words:
            transformed = [morse[ord(x)-ord('a')] for x in word]
            transformed_words.append(''.join(transformed))
        return len(set(transformed_words)) 
        