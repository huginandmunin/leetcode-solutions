class Solution:
    def numberToWords(self, num: int) -> str:
        """ Loop over digits in number, starting with least significant.
            Convert each digit to a word, based on power of 10.
            Concatenate of left side of output string.
        """
        str = ''
        power_of_10 = 0

        if num == 0:
            return 'Zero'

        while (num > 0):
            # Peel off least significant digit
            dig = num % 10
            num //= 10
            # Handle teens (in 10^0, 10^3, etc.)
            if (power_of_10 % 3 == 0) and (num % 10 == 1):
                dig += 10
                num //= 10
                p10_suffix = power_of_10
                power_of_10 += 1
            else:
                p10_suffix = power_of_10
            word = self.dig_to_word(dig,power_of_10)
            str = ' '.join((word,self.power_to_suffix(p10_suffix),str))
            power_of_10 += 1

        # Fix the extra spaces
        str = ' '.join(str.split())
        # Use string methods to remove 0 place holders
        str = str.replace('Thousand Hundred', 'Thousand')
        str = str.replace('Million Hundred', 'Million')
        str = str.replace('Billion Hundred', 'Billion')
        str = str.replace('Million Thousand', 'Million')
        str = str.replace('Billion Thousand', 'Billion')
        str = str.replace('Billion Million', 'Billion')
        return str


    def dig_to_word(self, dig, power_of_10):
        """ Convert each digit to a word depending on power of 10 """
        word = ''
        digits_dict = {
            0: {
                0: '',
                1: 'One',
                2: 'Two',
                3: 'Three',
                4: 'Four',
                5: 'Five',
                6: 'Six',
                7: 'Seven',
                8: 'Eight',
                9: 'Nine'
            },
            1: {
                0: '',
                1: 'Ten',
                2: 'Twenty',
                3: 'Thirty',
                4: 'Forty',
                5: 'Fifty',
                6: 'Sixty',
                7: 'Seventy',
                8: 'Eighty',
                9: 'Ninety',
                10: 'Ten',
                11: 'Eleven',
                12: 'Twelve',
                13: 'Thirteen',
                14: 'Fourteen',
                15: 'Fifteen',
                16: 'Sixteen',
                17: 'Seventeen',
                18: 'Eighteen',
                19: 'Nineteen',               
            }

        }
        if power_of_10 % 3 == 1:
            p10 = 1
        else:
            p10 = 0
        word = digits_dict[p10][dig]
        return word


    def power_to_suffix(self, power_of_10):
        suffix = ''
        power_suffix = {
            0: '',
            1: '',
            2: 'Hundred',
            3: 'Thousand',
            6: 'Million',
            9: 'Billion'
        }
        if power_of_10 in power_suffix.keys():
            p10 = power_of_10
        else:
            p10 = power_of_10 % 3
        suffix = power_suffix[p10]

        return suffix
