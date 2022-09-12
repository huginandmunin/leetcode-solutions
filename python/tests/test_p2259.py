from p2259_remove_digit_from_number_to_maximize_result import Solution

def test_solution1():
    solution = Solution()
    number = "123"
    digit = 3
    expected = "12"
    assert solution.removeDigit(number,digit)==expected

def test_solution2():
    solution = Solution()
    number = "1231"
    digit = 1
    expected = "231"
    assert solution.removeDigit(number,digit)==expected

def test_solution3():
    solution = Solution()
    number = "551"
    digit = 5
    expected = "51"
    assert solution.removeDigit(number,digit)==expected