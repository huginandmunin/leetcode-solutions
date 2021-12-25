from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        """
        Given a square matrix mat, return the sum of the matrix diagonals.

        Only include the sum of all the elements on the primary diagonal 
        and all the elements on the secondary diagonal that are not part 
        of the primary diagonal.
        """
        n=len(mat)        
        sumd = sum(mat[x][x]+mat[n-x-1][x] for x in range(n))
        # decrement by the double counted center square for odd length matrices.
        if n%2==1:
            sumd -= mat[n//2][n//2]
        return sumd