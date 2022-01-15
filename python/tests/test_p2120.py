from p2120_execution_of_all_suffix_instructions_staying_in_a_grid import Solution

def test_solution1():
    solution = Solution()
    n = 3
    startPos = [0,1]
    s = "RRDDLU" 
    expected = [1,5,4,3,1,0]
    assert solution.executeInstructions(n,startPos,s)==expected

def test_solution2():
    solution = Solution()
    n = 2
    startPos = [1,1]
    s = "LURD" 
    expected = [4,1,0,0]
    assert solution.executeInstructions(n,startPos,s)==expected

def test_solution3():
    solution = Solution()
    n = 1
    startPos = [0,0]
    s = "LRUD" 
    expected = [0,0,0,0]
    assert solution.executeInstructions(n,startPos,s)==expected