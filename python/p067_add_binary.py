class Solution:
    def addBinary(self, a: str, b: str) -> str:
        """ Given two binary strings a and b, return their sum as a binary string.
            The method below uses a list of characters. Reasonably fast.
            Add digit by digit starting with least significant bits.
        """

        if a =='0' and b == '0':
            return '0'

        result = ''
        carry = 0
        
        a_list = list(a)
        b_list = list(b)
        while a_list and b_list:
            
            sum = a_list.pop() + b_list.pop()
            if sum == '11':
                if carry == 1:
                    r = '1'
                else:
                    r = '0'
                    carry = 1
            elif (sum == '01' or sum == '10'):
                if carry == 1:
                    r = '0'
                else:
                    r = '1'
            else:
                r = str(carry)
                carry = 0
            result = r + result

        if a_list:
            result = self.list_to_result(a_list,carry,result)
        elif b_list:
            result = self.list_to_result(b_list,carry,result)
        else:
            if carry == 1:
                result = '1' + result
        return result


    def list_to_result(self,list,initial_carry,result):
        carry = initial_carry
        while list:
            sum = list.pop()
            print(f'in b, sum={sum}, carry = {carry}')
            if sum == '1':
                if carry == 1:
                    r = '0'
                else:
                    r = '1'
                    carry = 0
            else:
                if carry == 1:
                    r = str(carry)
                    carry = 0
                else:
                    r = '0'
            result = r + result

        if carry == 1:
            result = '1' + result
        return result
