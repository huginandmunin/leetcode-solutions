import sys
sys.path.append("..")

from p035_search_insert_position import Solution


def test_solution1():
    solution = Solution()
    input = [1,3,5,6]
    target = 5
    expected = 2
    assert solution.searchInsert(input,target)==expected

def test_solution2():
    solution = Solution()
    input = [1,3,5,6]
    target = 2
    expected = 1
    assert solution.searchInsert(input,target)==expected

def test_solution3():
    solution = Solution()
    input = [1,3,5,6]
    target = 7
    expected = 4
    assert solution.searchInsert(input,target)==expected

def test_solution4():
    solution = Solution()
    input = [1,3,5,6]
    target = 0
    expected = 0
    assert solution.searchInsert(input,target)==expected

def test_solution5():
    solution = Solution()
    input = [1]
    target = 0
    expected = 0
    assert solution.searchInsert(input,target)==expected

def test_solution6():
    solution = Solution()
    input = [1,3,5,6]
    target = 4
    expected = 2
    assert solution.searchInsert(input,target)==expected
