class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        """
        You're given strings jewels representing the types of stones 
        that are jewels, and stones representing the stones you have. 
        Each character in stones is a type of stone you have. 
        You want to know how many of the stones you have are also jewels.

        Letters are case sensitive, so "a" is considered a different 
        type of stone from "A".
        """
        count = 0
        for j in jewels:
            for s in stones:
                if s==j:
                    count += 1

        return count