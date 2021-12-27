from typing import List

class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        """
        You are given an m x n matrix mat and two integers r and c representing the number of 
        rows and the number of columns of the wanted reshaped matrix.

        The reshaped matrix should be filled with all the elements of the original 
        matrix in the same row-traversing order as they were.

        If the reshape operation with given parameters is 
        possible and legal, output the new reshaped matrix; Otherwise, 
        output the original matrix.
        """

        m = len(mat)
        n = len(mat[0])
        new_mat = [[]]

        if m==0 or n==0 or m*n != r*c:
            return mat

        k = 0
        l = 0
        for i in range(m):
            for j in range(n):
                new_mat[k].append(mat[i][j])
                l += 1
                if l % c == 0:
                    k += 1
                    l = 0
                    if k < r:
                        new_mat.append([])
        return new_mat


