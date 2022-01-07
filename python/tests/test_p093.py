from p093_restore_ip_addresses import Solution

def test_solution1():
    solution = Solution()
    s = "25525511135"
    expected = ["255.255.11.135","255.255.111.35"]
    assert solution.restoreIpAddresses(s)==expected

def test_solution2():
    solution = Solution()
    s = "0000"
    expected = ["0.0.0.0"]
    assert solution.restoreIpAddresses(s)==expected

def test_solution3():
    solution = Solution()
    s = "1111"
    expected = ["1.1.1.1"]
    assert solution.restoreIpAddresses(s)==expected

def test_solution4():
    solution = Solution()
    s = "010010"
    expected = ["0.10.0.10","0.100.1.0"]
    assert solution.restoreIpAddresses(s)==expected

def test_solution3():
    solution = Solution()
    s = "101023"
    expected = ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]
    assert solution.restoreIpAddresses(s)==expected