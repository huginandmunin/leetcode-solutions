import re

class Solution:
    def isPalindrome(self, s: str) -> bool:
        """ Remove non-alphanumeric characters, convert to lower
            and check if string is still a palindrome. 
        """

        s = re.sub(r'[^a-zA-Z0-9]','',s)
        return (s.lower() == s[::-1].lower())
