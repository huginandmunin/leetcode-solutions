from p2379_minimum_recolors_to_get_k_consecutive_black_blocks import Solution


def test_solution1():
    solution = Solution()
    blocks = "WBBWWBBWBW"
    k = 7
    expected = 3
    assert solution.minimumRecolors(blocks, k)==expected

def test_solution2():
    solution = Solution()
    blocks = "WBWBBBW"
    k = 2
    expected = 0
    assert solution.minimumRecolors(blocks, k)==expected

