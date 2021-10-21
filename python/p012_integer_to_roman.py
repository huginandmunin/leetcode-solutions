class Solution:
    def intToRoman(self, num: int) -> str:
        """ Convert integer to roman numeral """
        roman = ""
        power_of_10 = 0
        # Loop over digits in num, going least significant to most significant
        while (num > 0):
            n = num % 10
            # Convert each digit to a roman numeral, based on power of 10
            # and concatenate on left side of output string
            roman = self.get_roman(n, power_of_10) + roman
            num //= 10
            power_of_10 += 1

        return roman

    def get_roman(self, n: int, p: int):
        """ Convert n to roman, based on power of 10 """
        r = ""
        romans_dict = {
            0: {
                1: "I",
                5: "V"
            },
            1: {
                1: "X",
                5: "L"
            },
            2: {
                1: "C",
                5: "D"
            },
            3: {
                1: "M",
                5: ""
            }
        }

        if (n == 4):
            r = romans_dict[p][1] + romans_dict[p][5]
        elif (n == 9):
            r = romans_dict[p][1] + romans_dict[p+1][1]
        else:
            # This handles n=0, returns empty string
            n1 = n % 5
            n5 = int(n/5)
            r = romans_dict[p][5] * n5 + romans_dict[p][1] * (n1)
        return r

