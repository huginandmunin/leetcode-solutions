import re

class Solution:
    def isNumber(self, s: str) -> bool:
        """
        Given a string s, return true if s is a valid number.

        Use regular expression to see if string s matches this pattern:
          [+-]?(int|decimal)([eE][+-]?(int))?
        where decimal is
          (int)[.]|(int)[.](int)|[.](int)
        """

        # Check for match
        pattern = re.compile(r'^[+-]?(\d+|\d+\.|\.\d+|\d+\.\d+)([eE][+-]?\d+)?$')
        if re.match(pattern,s):
            return True

        return False