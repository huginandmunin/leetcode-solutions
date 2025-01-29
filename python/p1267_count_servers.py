from typing import List
from collections import Counter

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:
 
        rows_with_computers = []
        connected_servers = set()

        num_rows = len(grid)
        num_columns = len(grid[0])

        # hint 1: count computers in rows
        new_row_index = 0
        for row_index in range(num_rows):
            print(f"row = {grid[row_index]}")
            row_counts = Counter(grid[row_index])
            # maybe only store the rows with computers
            if row_counts[1] > 0:
                rows_with_computers.append(grid[row_index])
                if row_counts[1] > 1:
                    for column in range(num_columns):
                        if grid[row_index][column]==1:
                            connected_servers.add((new_row_index,column))
                new_row_index += 1


        print(f"rows_with_computers {rows_with_computers}")
        print(f"connected servers {connected_servers}")

        # how do I get the columns of the grid?
        # Like this: try this and see if the runtime improves.
        # grid = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        # column_index = 1  # Index of the column you want (0-based)
        # column = [row[column_index] for row in grid]
        # print(column)
        # then do the counts and adding on the column.
        #
        num_rows = len(rows_with_computers)
        for column_index in range(num_columns):
            column = [row[column_index] for row in rows_with_computers]
            column_counts = Counter(column)
            # only add columns with two or more servers
            if column_counts[1] > 1:
                for row_index in range(num_rows):
                    print(f"Ready to check {row_index}, {column_index}")
                    if rows_with_computers[row_index][column_index]==1:
                        connected_servers.add((row_index,column_index))



        # can I just transpose the grid to get the columns?
        # then search again but flip row and column
        # maybe use a suffix sum so we know when there are no more servers.

        # num_rows = len(rows_with_computers)
        # for row_index in range(len(rows_with_computers)):
        #     for column in range(num_columns):
        #         print(f"Working on {row_index}, {column}, grid {rows_with_computers[row_index][column]}")
        #         if rows_with_computers[row_index][column]==1:
        #             print("Searching down")
        #             for row_below in range(row_index+1, num_rows):
        #                 print(f"Inner loop {row_below}, {column}")
        #                 if rows_with_computers[row_below][column]==1:
        #                     print(f"Found server at {row_below}, {column}, grid {rows_with_computers[row_below][column]}")
        #                     connected_servers.add((row_index, column))
        #                     connected_servers.add((row_below, column))

                    
        print(f"connected servers = {connected_servers}")
        return len(connected_servers)




