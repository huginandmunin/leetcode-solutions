from p419_battleships_in_a_board import Solution

def test_solution1():
    solution = Solution()
    board = [["X",".",".","X"],[".",".",".","X"],[".",".",".","X"]]
    expected = 2
    assert solution.countBattleships(board)==expected


def test_solution2():
    solution = Solution()
    board = [["."]]
    expected = 0
    assert solution.countBattleships(board)==expected

def test_solution3():
    solution = Solution()
    board = [["X",".","."], ["X",".","."],["X",".","."]]
    expected = 1
    assert solution.countBattleships(board)==expected

def test_solution4():
    solution = Solution()
    board = [[".",".","."], [".",".","."],["X","X","X"]]
    expected = 1
    assert solution.countBattleships(board)==expected