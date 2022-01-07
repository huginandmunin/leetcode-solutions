from p169_majority_element import Solution


def test_solution1():
    solution = Solution()
    input = [3,2,3]
    expected = 3
    assert solution.majorityElement(input)==expected

def test_solution2():
    solution = Solution()
    input = [2,2,1,1,1,2,2]
    expected = 2
    assert solution.majorityElement(input)==expected