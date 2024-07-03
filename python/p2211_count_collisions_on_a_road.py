from typing import List

class Solution:
    def countCollisions(self, directions: str) -> int:
        """String version"""
        
        armed = False
        collisions = 0

        for c in directions:
            if c in ['R', 'S']:
                armed = True
                continue
            elif (c == 'L'):
                if armed:
                    collisions += 1


        # backward pass
        print("backward pass")
        armed = False
        for c in reversed(directions):
            if c in ['L', 'S']:
                armed = True
                continue
            elif (c == 'R'):
                if armed:
                    collisions += 1        

        return collisions

