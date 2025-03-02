from p121_best_time_to_buy_and_sell_stock import Solution

def test_solution1():
    solution = Solution()
    input = [7,1,5,3,6,4]
    expected = 5
    assert solution.maxProfit(input)==expected

def test_solution2():
    solution = Solution()
    input = [7,6,4,3,1]
    expected = 0
    assert solution.maxProfit(input)==expected
