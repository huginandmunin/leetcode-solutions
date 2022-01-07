from p205_isomorphic_strings import Solution


def test_solution1():
    solution = Solution()
    assert solution.isIsomorphic('egg','add')==True

def test_solution2():
    solution = Solution()
    assert solution.isIsomorphic('foo','bar')==False

def test_solution3():
    solution = Solution()
    assert solution.isIsomorphic('paper','title')==True

def test_solution4():
    solution = Solution()
    assert solution.isIsomorphic('badc','baba')==False
