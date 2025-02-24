class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
        """Use a stack"""

        s_stack = []
        len_part = len(part)

        for char in s:
            s_stack.append(char)
            if "".join(s_stack[-(len_part):])==part:
                # I think this line is slowing down the runtime
                s_stack = s_stack[:-(len_part)]

        return "".join(s_stack)