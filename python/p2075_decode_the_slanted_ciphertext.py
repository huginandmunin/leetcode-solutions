class Solution:
    def decodeCiphertext(self, encodedText: str, rows: int) -> str:
        """
        Solution gets number of columns and writes the encoded string
        into the matrix sequentially. Reading the diagonals will give
        the decoded string.
        """

        n = len(encodedText)
        cols = n // rows
        matrix = []
        result = ""

        # Write the encoded text into the matrix row by row
        encodedText = list(encodedText)
        start = 0
        end = cols
        [matrix.append(encodedText[start+i*cols:end+i*cols]) for i in range(rows)]

        # Read the diagonals
        for col in range(cols):
            i = 0
            j = col
            decoded = ""
            while i < rows and j < cols:
                decoded += matrix[i][j]
                i += 1
                j += 1
            result += decoded

        return result.rstrip()
