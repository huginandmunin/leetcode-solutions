from typing import List

class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """ Check a sudoku board for valid configuration. 
        """

        # Check number of rows in input
        board_size = 9
        if len(board) != board_size:
            return False

        # Find all groups that need checking
        # Rows
        for group in board:
            if not self.is_valid_group(group, board_size):
                return False
                
        # Check columns - number of rows and columns has been checked.
        for col in range(board_size):
            group = []
            for row in range(board_size):
                group.append(board[row][col])
            if not self.is_valid_group(group,board_size):
                return False

        # Subsquares
        sub_size = 3
        for sub_row in range(sub_size):
            for sub_col in range(sub_size):
                group = []
                for row in range(sub_size):
                    for col in range(sub_size):
                        group.append(board[row+(sub_row*3)][col+(sub_col*3)])
                if not self.is_valid_group(group,board_size):
                    return False

        return True

    def is_valid_group(self, num_list, board_size):
        """ Check if item is "." or in range 1-9.
            Check for repeats by adding numbers from list 
            into (non-repeating) set 
        """
        if len(num_list) != board_size:
            return False
        num_set = set()
        for num_str in num_list:
            # Check if "." or in 1-9
            if num_str != ".":
                if num_str.isnumeric():
                    num = int(num_str)
                    if not (num in range(1,board_size+1)):
                        return False
                    else: 
                        if num in num_set:
                            return False
                        else:
                            num_set.add(num)

                else:
                    # Not numeric
                    return False
            else:
                # dot is okay
                pass

        return True

