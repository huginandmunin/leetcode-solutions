from p001_two_sum import Solution


def test_solution1():
    solution = Solution()
    input = [2,7,11,15]
    target = 9
    expected = [0,1]
    assert solution.twoSum(input,target)==expected

def test_solution2():
    solution = Solution()
    input = [3,2,4]
    target = 6
    expected = [1,2]
    assert solution.twoSum(input,target)==expected

def test_solution3():
    solution = Solution()
    input = [3,3]
    target = 6
    expected = [0,1]
    assert solution.twoSum(input,target)==expected