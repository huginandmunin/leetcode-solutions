from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Given an m x n 2D binary grid grid which represents a map of 
        '1's (land) and '0's (water), return the number of islands.

        An island is surrounded by water and is formed by connecting 
        adjacent lands horizontally or vertically. You may assume all four 
        edges of the grid are all surrounded by water.

        Solution:  Start at (0,0) and look for land. 
        If found then increment counter and change grid value 
        from 1 to 2 all adjacent land (using the flood-fill method). 
        Step through grid checking for additional land.
        """

        result = 0
        land = "1"
        land_counted = "2"
        n_rows = len(grid)
        n_cols = len(grid[0])
        for i in range(n_rows):
            for j in range(n_cols):
                if grid[i][j]==land:
                    result += 1
                    grid = self.replaceColor(grid,i,j,land,land_counted)
                    
        return result 

    def replaceColor(self,image,sr,sc,oldColor,newColor):
        """
        Replace the color in cell and 4 nearest neighbors
        """
        if image[sr][sc]==oldColor:
            image[sr][sc]=newColor
            # recursively check neighbors, up, right, down, left
            if (sr>0 and image[sr-1][sc]==oldColor):
                image = self.replaceColor(image,sr-1,sc,oldColor,newColor)
            if (sc<len(image[sr])-1 and image[sr][sc+1]==oldColor):
                image = self.replaceColor(image,sr,sc+1,oldColor,newColor)
            if (sr<len(image)-1 and image[sr+1][sc]==oldColor):
                image = self.replaceColor(image,sr+1,sc,oldColor,newColor)
            if (sc>0 and image[sr][sc-1]==oldColor):
                image = self.replaceColor(image,sr,sc-1,oldColor,newColor)
        # return when all of the cells have been filled
        return image 

