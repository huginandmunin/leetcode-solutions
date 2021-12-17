from p412_fizz_buzz import Solution

def test_solution1():
    solution = Solution()
    n = 3
    expected = ["1","2","Fizz"]
    assert solution.fizzBuzz(n)==expected

def test_solution2():
    solution = Solution()
    n = 5
    expected = ["1","2","Fizz","4","Buzz"]
    assert solution.fizzBuzz(n)==expected

def test_solution2():
    solution = Solution()
    n = 15
    expected = ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
    assert solution.fizzBuzz(n)==expected