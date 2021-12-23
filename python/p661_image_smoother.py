from typing import List

class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        """
        An image smoother is a filter of the size 3 x 3 that can be applied 
        to each cell of an image by rounding down the average of the cell 
        and the eight surrounding cells (i.e., the average of the nine cells 
        in the blue smoother). If one or more of the surrounding cells of a cell 
        is not present, we do not consider it in the average (i.e., the average 
        of the four cells in the red smoother).

        The averaing algorithm was tedious to type up. It could be replaced with 
        two lines using a list comprehension.  
        """

        result = []

        for i in range(len(img)):
            result.append([])
            for j in range(len(img[0])):
                cell_avg = self.average_cells(i,j,img)
                result[i].append(cell_avg)
        return result

    def average_cells(self,row,col,img):
        s = img[row][col]
        count = 1
        if row > 0:
            s += img[row-1][col]
            count += 1
        if col < len(img[row])-1:
            s += img[row][col+1]
            count += 1
        if row > 0 and col < len(img[row])-1:
            s += img[row-1][col+1]
            count += 1
        if row < len(img)-1:
            s += img[row+1][col]
            count += 1
        if row < len(img)-1 and col < len(img[row])-1:
            s += img[row+1][col+1]
            count += 1
        if row < len(img)-1 and col > 0:
            s += img[row+1][col-1]
            count += 1
        if col > 0:
            s += img[row][col-1]
            count += 1
        if row > 0 and col > 0:
            s += img[row-1][col-1]
            count += 1
        return s // count

