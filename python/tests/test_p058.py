from p058_length_of_last_word import Solution

def test_solution1():
    solution = Solution()
    assert solution.lengthOfLastWord('Hello World')==5

def test_solution2():
    solution = Solution()
    assert solution.lengthOfLastWord('   fly me   to   the moon  ')==4

def test_solution3():
    solution = Solution()
    assert solution.lengthOfLastWord('luffy is still joyboy')==6

def test_solution4():
    solution = Solution()
    assert solution.lengthOfLastWord('z')==1

def test_solution5():
    solution = Solution()
    assert solution.lengthOfLastWord(' b')==1

def test_solution6():
    solution = Solution()
    assert solution.lengthOfLastWord(' b')==1