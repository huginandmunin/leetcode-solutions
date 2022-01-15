from typing import List

class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:

        results = []

        # Simulate movement to find number of completed instructions for each starting instruction
        for i in range(len(s)):
            count = 0
            pos = startPos
            for c in s[i:]:
                pos = self.go(pos,c)
                # Break if out of grid
                if pos[0] < 0 or pos[0] >= n or pos[1] < 0 or pos[1] >= n:
                    break                
                # If in grid then increment counter
                count += 1               
            results.append(count)
            
        return results

    def go(self,pos,c):
        """
        Grid rows increase going down and columns increase going right

        pos[0] = row, pos[1] = col

        0,0 0,1 0,2
        1,0 1,1 1,2
        2,0 2,1 2,2
        """
        if c == "L":
            return [pos[0], pos[1] - 1]
        if c == "U":
            return [pos[0] - 1, pos[1]]
        if c == "R":
            return [pos[0], pos[1] + 1]
        if c == "D":
            return [pos[0] + 1, pos[1]]


if __name__ == "__main__":
    solution = Solution()
    n = 3
    startPos = [0,1]
    s = "RRDDLU" 
    expected = [1,5,4,3,1,0]
    result = solution.executeInstructions(n,startPos,s)==expected