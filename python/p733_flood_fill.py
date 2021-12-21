from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        """
        An image is represented by an m x n integer grid image where image[i][j] represents the 
        pixel value of the image.

        You are also given three integers sr, sc, and newColor. 
        You should perform a flood fill on the image starting from the 
        pixel image[sr][sc].

        Hint 1: Write a recursive function that paints the pixel if it's the correct color, 
        then recurses on neighboring pixels.
        """

        # This is the color that will be replaced
        oldColor = image[sr][sc]
        if oldColor == newColor:
            return image

        self.replaceColor(image,sr,sc,oldColor,newColor)
        return image 

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