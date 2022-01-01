class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        """
        The Hamming distance between two integers is the number of 
        positions at which the corresponding bits are different.

        Given two integers x and y, return the Hamming distance between them.

        The method for counting '1's is very slow. It would be better to do a
        string.count('1') function instead of the list comprehension.
        """

        if x == y:
            return 0

        # Do an XOR sum of the numbers and convert to binary representation.
        xor_list = list(format(x^y,'b'))
        # Count the '1's in the string.
        return sum([1 for x in xor_list if x=='1'])
