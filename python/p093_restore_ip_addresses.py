from typing import List
import re

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        """
        Given a string s containing only digits, 
        return all possible valid IP addresses that can be formed 
        by inserting dots into s. You are not allowed to reorder or 
        remove any digits in s. 
        You may return the valid IP addresses in any order.
        """

        valid_ips = []

        # Form possible permutations. Check if each one is valid.
        for i in range(1,len(s)-2):
            ip1 = s[0:i]
            if not self.is_valid_number(ip1):
                continue
            for j in range(i+1, len(s)-1):
                ip2 = s[i:j]
                if not self.is_valid_number(ip2):
                    continue
                for k in range(j+1, len(s)):                  
                    ip3 = s[j:k]
                    ip4 = s[k:len(s)]
                    if ( self.is_valid_number(ip3) and self.is_valid_number(ip4) ):
                        valid_ips.append('.'.join([ip1,ip2,ip3,ip4]))

        return valid_ips


    def is_valid_number(self, number_str: str):
        """
        Valid if number <= 255 and does not have 0 followed by digit. Single 0 is okay. 
        """
        if int(number_str) > 255:
             return False
        if re.match(r'0+\d',number_str):
            return False
        return True


if __name__ == "__main__":
    solution = Solution()


    s = "25525511135"
    print(f'result = {solution.restoreIpAddresses(s)}')

    s = "0000"
    print(f'result = {solution.restoreIpAddresses(s)}')

    s = "1111"
    print(f'result = {solution.restoreIpAddresses(s)}')

    s = "010010"
    print(f'result = {solution.restoreIpAddresses(s)}')

    s = "101023"
    print(f'result = {solution.restoreIpAddresses(s)}')