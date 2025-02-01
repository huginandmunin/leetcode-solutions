from typing import List

class Solution:
    def gridGame(self, grid: List[List[int]]) -> int:
        """Hint 2: Can we use prefix sums to help solve this problem?
        
        If the red robot transitions from the top row (t) to the bottom (b)
        at some index, i, what are the options for the blue robot?

        The two possible options for blue are either what remains in 
        the top row or what has not been selected in the bottom row
        as shown below:

        0    0    ... 0      0 t[i+1] ... t[n-1]
                             |
                             |
        b[0] b[1] ... b[i-1] 0 0      ... 0

        Blue can select the maximum of sum(t[i+1], ..., t[n-1]) and
        sum(b[0], b[1], ..., b[i-1]).

        We can think of construction an array of the maximums for any
        transition point:

        max[0], max[1], ... max[n-1]

        The strategy for for red would be to transition at the index that 
        corresponds to the minimum in the maximums array.

        The options for blue can constructed with a suffix sum for the top row
        and a prefix sum for the bottom row. Then for a general index where 
        red can tranisition, the best option for blue is

        max[i] = max(suffix[i+1], prefix[i-1])

        The edge cases are when red would transition at 0 or n-1:
        max[0] = suffix[1]
        max[n-1] = prefix[n-2]

        The maximums array is helpful for illustrative purposes. But
        we could actually keep a running selection of encountered minimums.
        
        """
        
        array_length = len(grid[0])

        # handle edge cases
        if array_length == 1:
            return 0
        
        if array_length == 2:
            return min(grid[0][1], grid[1][0])

        top = grid[0]    
        sum = 0
        suffix = [0] * array_length
        for i in range(array_length-1, -1, -1):
            sum += top[i]
            suffix[i] = sum

        bottom = grid[1]
        sum = 0
        prefix = []
        for num in bottom:
            sum += num
            prefix.append(sum)

        # Iterate over indexes and find blue's possible scores
        # maximums_array = [suffix[1]]
        best_score = suffix[1]
        for i in range(1,array_length-1):
            max_i = max(suffix[i+1], prefix[i-1])
            # maximums_array.append(max_i)
            best_score = min(best_score, max_i)
        # maximums_array.append(prefix[array_length-2])
        best_score = min(best_score, prefix[array_length-2])

        return best_score
