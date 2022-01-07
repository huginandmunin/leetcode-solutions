from typing import List

class Solution:
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        """
        Return a 2D array containing the 4-length arrays described above 
        for each group of farmland in land. If there are no groups of farmland, 
        return an empty array. You may return the answer in any order.

        Solution:  Start at position (0,0) and look for farmland. 
        If found then recursively apply a flood-fill method. Since 
        the regions are rectangular we only have to check to the right and
        down. Set the region upper-left and lower-right positions after all 
        neighbors have been checked. 

        Step through grid checking for additional farm land.
        """

        result = []
        landColor = 1
        newColor = 2

        def replaceColor(sr,sc):
            """
            Replace the color in cell and to right and down
            """
            # row and column indeces to return
            ir = id = sr
            jr = jd = sc

            if land[sr][sc]==landColor:
                land[sr][sc]=newColor
                # recursively check neighbors, right and down
                if (sc<len(land[sr])-1 and land[sr][sc+1]==landColor):
                    ir, jr = replaceColor(sr,sc+1)
                if (sr<len(land)-1 and land[sr+1][sc]==landColor):
                    id, jd = replaceColor(sr+1,sc)
            # return when all of the cells have been filled
            mr = max(ir,id)
            mc = max(jr,jd)
            return mr,mc

        # step through arrays
        for i in range(len(land)):
            for j in range(len(land[0])):
                if land[i][j] == landColor:
                    # Find extent of region
                    endi, endj = replaceColor(i,j)
                    # set endpoints of region
                    region = [i,j,endi,endj]
                    result.append(region)         
        return result 

    