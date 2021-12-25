from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        """
        Write an efficient algorithm that searches for a value in an 
        m x n matrix. This matrix has the following properties:

        -Integers in each row are sorted from left to right.
        -The first integer of each row is greater than the last integer 
        of the previous row.

        Solution implements (1) a binary search on the first column and
        then (2) a binary search on the target row. 
        
        This should be O(m+n). A brute-force grid search would be O(m*n).
        """

        m = len(matrix)
        n = len(matrix[0])

        # Check if target is outside the values of the matrix        
        if target < matrix[0][0] or target > matrix[m-1][n-1]:
            return False
       
        # Grab the first column, identify which row might have the target
        first_col = [matrix[x][0] for x in range(m)]
        top = 0
        bot = m-1
        i = self.search_in_list(top, bot, first_col, target)
        print(f'Target row from i={i}')

        # Check if we have the target in first column.
        if matrix[i][0]==target:
            return True

        # Pull out the corresponding row, search for target in this row
        row = matrix[i]
        left = 0
        right = n-1
        print(f'Target row ={row}')
        j = self.search_in_list(left, right, row, target)
        if matrix[i][j]==target:

            return True

        # Did not find target
        return False


    def search_in_list(self, l: int, r: int, nums: List, target: int):
        """
        Binary search for target in list. Return lower bound index of
        target.
        """
        middle = (l + r) // 2
        middle_val = nums[middle]
        print(f'In search, l={l}, r={r}, mid={middle}')
        print(f'numl={nums[l]}, num_mid={middle_val}, numr={nums[r]}')
        if target < nums[l] or target==nums[l]:
            return l 
        elif l==r or middle_val == target:
            return middle                  
        elif target > nums[r] or target==nums[r]:
            return r
        elif l==middle or r==middle:
            return middle
        elif target < middle_val:
            r = middle
        else:
            l = middle
        print(f'Searching l={l}, r={r}')
        middle = self.search_in_list(l,r,nums,target)
        return middle

 