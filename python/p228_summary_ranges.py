from typing import List

class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:

        if not nums:
            return []

        ranges = []
        # print(f'input={nums}')
        prev_num = nums.pop(0)
        this_range = [prev_num]
        for num in nums:
            # print(f'num={num}, prev={prev_num}')
            if num > prev_num + 1:
                this_range.append(prev_num)
                ranges.append(this_range)
                this_range = [num]
            # print(f'this range = {this_range}')
            prev_num = num

        # Handle last number
        this_range.append(prev_num)
        ranges.append(this_range)

        # Reformat lists of ints into list of strings.
        ranges_str = []
        for range in ranges:
            if range[0]==range[1]:
                ranges_str.append(f'{range[0]}')
            else:
                ranges_str.append(f'{range[0]}->{range[1]}')

        return ranges_str


if __name__ == '__main__':
    solution = Solution()
    input = [0,1,2,4,5,7]
    result = solution.summaryRanges(input)
    print(f'input={input}, result={result}')

    input = [0,2,3,4,6,8,9]
    result = solution.summaryRanges(input)
    print(f'input={input}, result={result}')

    input = [0,2,5,8,11]
    result = solution.summaryRanges(input)
    print(f'input={input}, result={result}')

    input = []
    result = solution.summaryRanges(input)
    print(f'input={input}, result={result}')

    input = [-1]
    result = solution.summaryRanges(input)
    print(f'input={input}, result={result}')

    input = [-5,-4,-3,-1,0,1,4,6]
    result = solution.summaryRanges(input)
    print(f'input={input}, result={result}')