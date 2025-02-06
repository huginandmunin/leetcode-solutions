from collections import Counter
from typing import List

class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:

        products = {}
        num_tuples = 0

        # find possible products
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                product = nums[i] * nums[j]
# 
                # store the products in a dict
                if product in products.keys():
                    products[product].append((nums[i], nums[j]))
                else:
                    products[product] = [(nums[i], nums[j])]

        print(f"Products {products}")

        # find products that repeat more than once
        # each set of two pairs can give 8 permutations
        # each group of n pairs can form n(n-1)/2 sets of two pairs.
        for key, value in products.items():
            n = len(value)
            if n >= 2:
                combination = int(n * (n-1) / 2)
                num_tuples += 8 * combination

        return num_tuples

