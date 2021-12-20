from typing import List

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        """
        You are given row x col grid representing a map where grid[i][j] = 1 
        represents land and grid[i][j] = 0 represents water.

        Grid cells are connected horizontally/vertically (not diagonally). 
        The grid is completely surrounded by water, and there is exactly one 
        island (i.e., one or more connected land cells).

        The island doesn't have "lakes", meaning the water inside isn't 
        connected to the water around the island. One cell is a square with 
        side length 1. The grid is rectangular, width and height don't exceed 100. 
        Determine the perimeter of the island.
        """

        result = 0
        # Find edges. Edges have length=1 so
        # perimeter=sum of edges.
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                result += self.find_edges_for_cell(i,j,grid)
        return result

    def find_edges_for_cell(self, i: int, j: int, grid: List[List[int]]):
        """
        Edges are formed where cell is non-zero and nearest neighbors have a 
        different value (=0).
        Check up, right, down, and left. 
        """
        n = 0
        if grid[i][j]:
            if (i==0 or (i>0 and grid[i-1][j]==0)):
                n += 1
            if (j==len(grid[i])-1 or (j<len(grid[i])-1 and grid[i][j+1]==0)):
                n += 1
            if (i==len(grid)-1 or (i<len(grid)-1 and grid[i+1][j]==0)):
                n += 1
            if (j==0 or (j>0 and grid[i][j-1]==0)):
                n += 1
        return n
