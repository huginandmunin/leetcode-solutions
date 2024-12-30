from typing import List

class Solution:
    def reverseVowels(self, s: str) -> str:
        """
        Given a string s, reverse only all the vowels in the string and return it.
        """

        # front and end of the string
        front = 0
        end = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        chars = list(s)

        while front < end:
            if chars[front] in vowels and chars[end] in vowels:
                tmp = chars[front]
                chars[front] = chars[end]
                chars[end] = tmp
                front += 1
                end -= 1

            else:
                while not chars[front] in vowels and front < end:
                    front += 1
                while not chars[end] in vowels and end > front:
                    end -= 1
                    
            if front >= end:
                break

        return ''.join(chars)

        