class Solution:
    def reverseBits(self, n: int) -> int:
        """
        Reverse bits of a given 32 bits unsigned integer.
        """
        # Convert to binary string, remove leading '0b', reverse string
        n = bin(n)[-1:1:-1]
        # Pad to length 32 to recover any leading 0's that were lost by bin function.
        n += '0' * (32-len(n))
        # Convert back to int.
        return int(n,2)