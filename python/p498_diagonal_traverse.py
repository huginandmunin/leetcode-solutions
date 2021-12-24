from typing import List

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        """
        Given an m x n matrix mat, return an array of 
        all the elements of the array in a diagonal order.
        """
        result = []
        m = len(mat)
        n = len(mat[0])

        # Start at (0,0)
        r,c = 0,0
        result.append(mat[r][c])
        dir = "up"
        count = 1
        
        while(count < m*n):
            count += 1
            r,c,dir = self.get_next_cell(m,n,r,c,dir)
            result.append(mat[r][c])
            print(f'count={count}, result={result}')

        return result

    def get_next_cell(self,m,n,r,c,dir):
        """
        Going up:
        If at last column then row+=1 and dir changes from up to down.
        If at top row the cell+=1 and dir changes from up to down. 
        Else row-=1,col+=1
        Going down:
        If at last row then col+=1 and dir changes from down to up.
        If at last column then row+=1 and dir changes from up to down.
        Else row+=1,col-=1       
        """
        if dir == "up":
            if c == n-1:
                return r+1, c, "down"
            elif r == 0: 
                return r, c+1, "down"
            else:
                return r-1, c+1, "up"
        else:
            if r == m-1:
                return r, c+1, "up"
            if c == 0: 
                return r+1, c, "up"
            else:
                return r+1, c-1, "down"


if __name__ == "__main__":
    solution = Solution()
    mat = [[1]]
    result = solution.findDiagonalOrder(mat)
    print(f'Result = {result}')