from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        found = set()
        for num in nums:
            if num >= 1:
                found.add(num)

        if 1 not in found:
            return 1
        prev = 1
        print("Starting loop")
        for num in found:
            print(f"Testing num={num} and prev={prev}")
            if num - prev > 1:
                return prev + 1
            prev = num

        return num + 1
