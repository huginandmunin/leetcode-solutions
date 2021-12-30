from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """
        Given an m x n matrix, return all elements of the matrix in spiral order.

        Following the hints, this solutions implements a brute-force simulation.
        """

        if len(matrix)==1 and len(matrix[0])==1:
            return [matrix[0][0]]
        
        m = len(matrix)
        n = len(matrix[0])

        min_row = 0
        max_row = m-1
        min_col = 0
        max_col = n-1

        # Start at 0,0 and move to right. 
        count = 1
        i = 0
        j = 0
        result=[matrix[i][j]]
        if n == 1:
            dir = "down"
        else:
            dir = "right"
        while (count < m*n):
            if dir == "right":
                j += 1
                if j == max_col:
                    dir = "down"                    
                    min_row += 1
            elif dir == "down":
                i += 1
                if i == max_row:
                    dir = "left"
                    max_col -= 1
            elif dir == "left":
                j -= 1
                if j == min_col:
                    dir = "up"
                    max_row -= 1                    
            elif dir == "up":
                i -= 1
                if i == min_row:
                    dir = "right"
                    min_col += 1
            result.append(matrix[i][j])
            count += 1

        return result
