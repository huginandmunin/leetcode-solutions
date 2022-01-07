from typing import List

class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        """
        Given an m x n matrix board where each cell is a battleship 'X' or empty '.', 
        return the number of the battleships on board.

        Solution is similar to P200 Number of Islands:
        Start at position(0,0) and look for battleship. 
        If found then increment counter and change grid value 
        from "X" to "Y" for all adjacent positions with a battleship 
        (using the flood-fill method to flag a battleship that has been found). 
        Step through remainder of grid checking for additional battleships.

        The followup question suggests that there is a possible solution
        that does not require changing values in the board. 
        1. Keep a list of positions that have a battleship.
        2. If position has target, compare against adjacent up and left positions for empty spaces
        (no recursion, no changing values, no lists of visited positions). 
        """

        result = 0
        shipColor = "X"
        shipCounted = "Y"
        n_rows = len(board)
        n_cols = len(board[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if board[i][j]==shipColor:
                    result += 1
                    board = self.replaceColor(board,i,j,shipColor,shipCounted)
                    
        return result 


    def replaceColor(self,image,sr,sc,oldColor,newColor):
        """
        Replace the color in cell and nearest neighbors down and to right. 
        """
        if image[sr][sc]==oldColor:
            image[sr][sc]=newColor
            # recursively check neighbors to right and down
            if (sc<len(image[sr])-1 and image[sr][sc+1]==oldColor):
                image = self.replaceColor(image,sr,sc+1,oldColor,newColor)
            if (sr<len(image)-1 and image[sr+1][sc]==oldColor):
                image = self.replaceColor(image,sr+1,sc,oldColor,newColor)
        # return when all of the cells have been filled
        return image 

if __name__ == "__main__":
    solution = Solution()
    board = [["X",".","."], ["X",".","."],["X",".","."]]
    result = solution.countBattleships(board)