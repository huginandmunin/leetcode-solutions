class Solution:
    def reverseWords(self, s: str) -> str:
        """ Use standard string methods of split and join. 
            This method is slow but doesn't use much memory.
        """
        list = s.split()
        js = list.pop()
        while(list):
            js = f"{js} {list.pop()}"
        return js