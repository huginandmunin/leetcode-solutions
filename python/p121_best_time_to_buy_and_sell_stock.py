from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Run a Kadane's algorithm (P53) on a first derivative,
        the profits per day.
        """
        

        if len(prices) < 2:
            return 0

        # first derivative is profits per day
        profits = []
        for i in range(1, len(prices)):
            profits.append(prices[i] - prices[i-1])

        # find the maximum subarray sum, ie, the
        # maximum profits of a subarray of profits
        local_max = profits[0]
        global_max = profits[0]

        for i in range(1, len(profits)):
            local_max = max(local_max + profits[i], profits[i])
            global_max = max(global_max, local_max)
        
        # if best profits are negative then don't buy and sell anything
        if global_max < 0:
            global_max = 0
            
        return global_max
    


if __name__ == '__main__':
    solution = Solution()

    input = [7,1,5,3,6,4]
    result = solution.maxProfit(input)
    print(f"input={input}, Result = {result}")

    input = [7,6,4,3,1]
    result = solution.maxProfit(input)
    print(f"input={input}, Result = {result}")
