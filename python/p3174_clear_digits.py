import re
class Solution:
    def clearDigits(self, s: str) -> str:
        """The regex is naive and a bit clunky. A stack is more efficient."""

        pattern = ".*(\D\d).*"
        group = re.match(pattern, s)
        while group is not None:
            s = s.replace(group[1], "")
            group = re.match(pattern, s)
            print(f"Group = {group}")

        return(s)


