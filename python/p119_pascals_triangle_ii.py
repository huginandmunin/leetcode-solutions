from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        new_row = []
        edge_val = 1
        prev_row = row1 = [1]
        if rowIndex == 0:
            return row1
        for i in range(rowIndex):
            new_row = self.create_row(prev_row, edge_val)
            prev_row = new_row

        return new_row

    def create_row(self, prev_row, edge_val):
        new_row = [edge_val]
        for i in range(len(prev_row)-1):
            new_row.append(prev_row[i] + prev_row[i+1])
        new_row.append(edge_val)
        return new_row