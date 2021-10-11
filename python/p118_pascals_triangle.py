from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        edge_val = 1
        prev_row = row1 = [1]
        out_list = [row1]
        for i in range(1,numRows):
            new_row = self.create_row(prev_row, edge_val)
            out_list.append(new_row)
            prev_row = new_row

        return out_list

    def create_row(self, prev_row, edge_val):
        new_row = [edge_val]
        for i in range(len(prev_row)-1):
            new_row.append(prev_row[i] + prev_row[i+1])
        new_row.append(edge_val)
        return new_row

