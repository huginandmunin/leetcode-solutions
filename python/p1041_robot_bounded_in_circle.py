class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        """
        Return True if returns to 0,0 or changes direction at end of instructions.
        """

        # Up, left, down, right
        directions = [0,1,2,3]
        x = 0
        y = 0
        direction = 0

        # Check for change in direction
        n_left = instructions.count("L")
        n_right = instructions.count("R")
        if (n_left > 0 or n_right > 0) and (n_left != n_right) and ((n_left - n_right) % 4 != 0):
            return True

        # Now try the simulation
        for i in instructions:
            if i == 'G':
                x,y = self.go(direction,x,y)
            else:
                direction = self.change_dir(direction,i)

        if direction != 0 or (x==0 and y==0):
            return True
        else:
            return False


    def go(self, direction, x, y):
        if direction==0:
            return x, y+1
        elif direction==1:
            return x-1, y
        elif direction==2:
            return x, y-1
        else:
            return x+1, y


    def change_dir(self,direction,instruction):
        if instruction=="L":
            return (direction+1) % 4
        else:
            return (direction-1) % 4
