from p2073_time_needed_to_buy_tickets import Solution


def test_solution1():
    solution = Solution()
    tickets = [2,3,2]
    k=2
    expected=6
    assert solution.timeRequiredToBuy(tickets,k)==expected

def test_solution2():
    solution = Solution()
    tickets = [5,1,1,1]
    k=0
    expected=8
    assert solution.timeRequiredToBuy(tickets,k)==expected

def test_solution3():
    solution = Solution()
    tickets = [0,0,0,0,0,0,0,0,0,99]
    k=9
    expected=99
    assert solution.timeRequiredToBuy(tickets,k)==expected

def test_solution3():
    solution = Solution()
    tickets = [84,49,5,24,70,77,87,8]
    k=3
    expected=154
    assert solution.timeRequiredToBuy(tickets,k)==expected

