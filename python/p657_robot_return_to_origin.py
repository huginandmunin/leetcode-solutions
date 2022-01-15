class Solution:
    def judgeCircle(self, moves: str) -> bool:
        """
        Don't simulate. Use string count method to check if
        number-left==number-right 
        and
        number-up==number-down
        """

        return (moves.count('L')==moves.count('R') and moves.count('U')==moves.count('D'))