class Solution:
    def sortSentence(self, s: str) -> str:
        """
        Given an input sentences (with words and concatinated numbers)
        sort the sentence and strip out the numbers, eg,
        "is2 sentence4 This1 a3" -> "This is a sentence"

        If the digits were larger than 9 then I would strip out the number
        with a regex. Otherwise, we can use list indexing. 
        """

        # Get a dict where the key is the stripped out number, {2: 'is'}, etc.
        sdict = {x[len(x)-1:len(x)]:x[:len(x)-1] for x in s.split(' ')}
        # Select the word portion from the sorted items
        slist = [x[1] for x in sorted(sdict.items())]
        return ' '.join(slist)
