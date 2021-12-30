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
        #for i in range(rows):
        #    matrix.append(encodedText[start:end])
        #    start += cols
        #    end += cols
            # print(f'i={i}, matrix={matrix}')

        # Read the diagonals
        for col in range(cols):
            i = 0
            j = col
            decoded = ""
            while i < rows and j < cols:
                # print(f'Adding i={i}, j={j}, matrix={matrix[i][j]}')
                decoded += matrix[i][j]
                i += 1
                j += 1
            result += decoded
            # print(f'result = {result}')

        return result.rstrip()


if __name__ == "__main__":
    solution = Solution()
    encodedText = "ch   ie   pr"
    rows = 3
    result = solution.decodeCiphertext(encodedText,rows)