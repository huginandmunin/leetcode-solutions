from typing import List

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
 
        # if equal then return true
        if mat == target:
            return True

        # try rotating up to 3 more times.
        dim = len(mat[0])
        for rotation_count in range(3):

            # this whole block can be replaced by 1 line using a list comprehension
            rotated_mat = []
            for i in range(dim):
                rotated_mat.append([])
                for j in range(dim):
                    rotated_mat[i].append(0)
            for i in range(dim):
                for j in range(dim):
                    rotated_mat[j][dim-1-i] = mat[i][j]
            mat = rotated_mat

            if mat == target:
                return True
            
        # else return False
        return False
