from p027_remove_element import Solution


def test_solution1():
    solution = Solution()
    input = [3,2,2,3]
    target = 3
    expected = 2
    assert solution.removeElement(input,target)==expected

def test_solution2():
    solution = Solution()
    input = [0,1,2,2,3,0,4,2]
    target = 2
    expected = 5
    assert solution.removeElement(input,target)==expected