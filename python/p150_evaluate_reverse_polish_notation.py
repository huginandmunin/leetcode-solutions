from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        Numbers get pushed into stack.
        Operands will pull out two numbers and will append the result.
        """

        def operate(int1, int2, operator):
            if operator == '+':
                return int1 + int2
            if operator == '-':
                return int1 - int2
            if operator == '*':
                return int1 * int2
            if operator == '/':
                # This part can be replaced with 'int(int1/int2)'
                if (int1 < 0) ^ (int2 < 0):
                    sign = -1
                else:
                    sign = 1 
                result = abs(int1) // abs(int2)
                result *= sign
                return result
            

        stack = []
        operators = ["+","-","*","/"]

        for item in tokens:
            print(f"Item = {item}")

            # If operand then pull out two numbers from stack, 
            # operate, and push result back into stack.
            if item in operators:
                int2 = stack.pop()
                int1 = stack.pop()
                result = operate(int1, int2, item)
                stack.append(result)

            # If number then push into stack
            else:
                stack.append(int(item))

            print(f"Stack {stack}")

        # Hopefully we have just one number left in our stack
        return stack.pop()
