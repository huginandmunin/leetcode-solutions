from typing import List

class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        """
        Given an m x n matrix, return true if the matrix is Toeplitz. 
        Otherwise, return false.

        A matrix is Toeplitz if every diagonal from top-left to bottom-right 
        has the same elements.
        """

        # For each cell, check that cells down-right are the same value
        # A faster runtime can be obtained by comparing slices of adjacent rows
        # instead of cell-by-cell. 
        for row in range(len(matrix)-1):
            for col in range(len(matrix[row])-1):
                if matrix[row][col]!=matrix[row+1][col+1]:
                    return False

        return True