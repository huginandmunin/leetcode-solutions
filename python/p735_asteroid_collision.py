from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:

        new_asteroids = []
        for asteroid in asteroids:
            # add new asteroid to right side of stable list of asteroids
            self.add_asteroid(new_asteroids, asteroid)

        return new_asteroids

     
    def add_asteroid(self, new_asteroids, asteroid):
            
            # stable - adding new to an empty list
            if len(new_asteroids) == 0:
                new_asteroids.append(asteroid)
                return

            right = new_asteroids[-1]

            # stable - moving in the same direction
            if (
                right >= 0 and asteroid >= 0
            ) or (
                right < 0 and asteroid < 0
            ):
                new_asteroids.append(asteroid)
                print(f"Stable new = {new_asteroids}, asteroid = {asteroid}")
                return

            # stable - moving in opposite directions
            if right < 0 and asteroid >= 0:
                new_asteroids.append(asteroid)
                return

            # collision
            if right >= 0 and asteroid < 0:
                if abs(right) > abs(asteroid):
                    # asteroid explodes - now stable
                    return
        
                if abs(right) == abs(asteroid):
                    # both explode, remove right and continue to next asteroid
                    new_asteroids.pop()
                    return


                if abs(right) < abs(asteroid):
                    # right explodes, recursively check for additional right explosions
                    new_asteroids.pop()
                    self.add_asteroid(new_asteroids, asteroid)

    