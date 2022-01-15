import re

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        # True if all caps, first letter only, or all lower case
        if re.match("^[A-Z]{0,1}([A-Z]*|[a-z]*)$",word):
            return True
        else:
            return False