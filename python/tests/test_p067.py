from p067_add_binary import Solution


def test_solution1():
    input1 = '11'
    input2 = '1'
    solution = Solution()
    expected = '100'
    assert solution.addBinary(input1,input2)==expected


def test_solution2():
    input1 = '11'
    input2 = '1101'
    solution = Solution()
    expected = '10000'
    assert solution.addBinary(input1,input2)==expected


def test_solution3():
    input1 = '1010'
    input2 = '1011'
    solution = Solution()
    expected = '10101'
    assert solution.addBinary(input1,input2)==expected


def test_solution4():
    input1 = '100'
    input2 = '110010'
    solution = Solution()
    expected = '110110'
    assert solution.addBinary(input1,input2)==expected

def test_solution5():
    input1 = '10101'
    input2 = '1010'
    solution = Solution()
    expected = '11111'
    assert solution.addBinary(input1,input2)==expected