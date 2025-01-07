from p1769_minimum_number_of_operations_to_move_all_balls_to_each_box import Solution

# def test_solution1():
#     solution = Solution()
#     boxes = "110"
#     expected = [1,1,3]
#     assert solution.minOperations(boxes)==expected

# def test_solution2():
#     solution = Solution()
#     boxes = "001011"
#     expected = [11,8,5,4,3,4]
#     assert solution.minOperations(boxes)==expected

def test_solution3():
    solution = Solution()
    boxes = "0"
    expected = [0]
    assert solution.minOperations(boxes)==expected