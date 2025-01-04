from p150_evaluate_reverse_polish_notation import Solution


def test_solution1():
    solution = Solution()
    tokens = ["2","1","+","3","*"]
    expected = 9
    assert solution.evalRPN(tokens)==expected

def test_solution2():
    solution = Solution()
    tokens = ["4","13","5","/","+"]
    expected = 6
    assert solution.evalRPN(tokens)==expected

def test_solution3():
    solution = Solution()
    tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
    expected = 22
    assert solution.evalRPN(tokens)==expected