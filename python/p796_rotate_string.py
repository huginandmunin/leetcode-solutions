class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        """
        Given two strings s and goal, return true if and only if 
        s can become goal after some number of shifts on s.

        A shift on s consists of moving the leftmost character of s 
        to the rightmost position.
        """

        # Can shift via string slicing until s == goal
        for i in range(len(s)):
            if s == goal:
                return True
            s = s[1:]+s[0:1]
        return False

