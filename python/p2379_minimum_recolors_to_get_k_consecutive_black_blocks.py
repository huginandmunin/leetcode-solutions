class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        """Use a prefix sum"""
        # sum = 0
        # prefix = []
        # minimum = 0
        # for i in range(len(blocks)):
        #     if blocks[i] == "B":
        #         sum += 1
        #     prefix.append(sum)
        # operations = k - prefix[k-1]
        # if operations == 0:
        #     return operations
        # minimum = operations
        # for i in range(k, len(prefix)):
        #     operations = k - (prefix[i] - prefix[i - k])
        #     minimum = min(minimum, operations)

        # return minimum

        
        """Use a sliding window"""
        is_black = []
        for char in blocks:
            if char == "B":
                is_black.append(1)
            else:
                is_black.append(0)
        
        window_sum = sum(is_black[:k])
        operations = k - window_sum
        minimum = operations
        for i in range(k, len(blocks)):
            # window_sum = window_sum + is_black[i] - is_black[i - k]
            # operations = k - window_sum
            # the above two lines can be written like this
            operations = operations + is_black[i-k] - is_black[i]
            minimum = min(minimum, operations)

        return minimum
