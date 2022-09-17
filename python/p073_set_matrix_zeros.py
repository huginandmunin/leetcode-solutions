from typing import List

class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        rows = len(matrix)
        cols = len(matrix[0])
        target = 0
        zeroes = []

        # Get locations of zeros on first pass
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == target:
                    zeroes.append([r, c])

        # Set the rows and columns
        for pair in zeroes:
            for c in range(cols):
                matrix[pair[0]][c] = target
            for r in range(rows):
                matrix[r][pair[1]] = target

        return matrix
