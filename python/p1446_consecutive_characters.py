class Solution:
    def maxPower(self, s: str) -> int:
        """
        The power of the string is the maximum length of a non-empty 
        substring that contains only one unique character.

        Given a string s, return the power of s.
        """
        if len(s)==1:
            return 1
        power = 0
        count = 0
        prev = s[0]
        for x in s:
            if x == prev:
                count += 1
            else:
                power = max(power,count)
                prev = x
                count = 1
        power = max(power,count)
        return power
