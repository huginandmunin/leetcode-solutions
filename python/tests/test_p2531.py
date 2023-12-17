from p2531_make_number_of_distinct_characters_equal import Solution

def test_solution1():
    solution = Solution()
    word1 = "ac"
    word2 = "b"
    expected = False
    assert solution.isItPossible(word1,word2)==expected

def test_solution2():
    solution = Solution()
    word1 = "abc"
    word2 = "ab"
    expected = True
    assert solution.isItPossible(word1,word2)==expected

def test_solution3():
    solution = Solution()
    word1 = "abcde"
    word2 = "fghij"
    expected = True
    assert solution.isItPossible(word1,word2)==expected

def test_solution4():
    solution = Solution()
    word1 = "ab"
    word2 = "abcc"
    expected = False
    assert solution.isItPossible(word1,word2)==expected

def test_solution5():
    solution = Solution()
    word1 = "abcc"
    word2 = "aab"
    expected = True
    assert solution.isItPossible(word1,word2)==expected

def test_solution6():
    solution = Solution()
    word1 = "fkhjcmmsncaoopccdidfcerfbrfraiskoabaraqxprdxiqpxxenmdhsnsohnfkmolaakjjijbxlijngjnlqrpdqrirgmfdjmmnqbbjnxardxoqlkjmlabghxxrjs"
    word2 = "nocobbrohjrejrmllfmfdbkqprijcrjjpmfjcrfdinahqgeshfekchqklklohnpiaogepbogbdcombrlkipfppsjohefhofmpmmcfbdbcmgb"
    expected = True
    assert solution.isItPossible(word1,word2)==expected

def test_solution7():
    solution = Solution()
    word1 = "eeeee"
    word2 = "eeeee"
    expected = True
    assert solution.isItPossible(word1,word2)==expected