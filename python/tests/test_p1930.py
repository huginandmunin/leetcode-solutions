from p1930_unique_length_3_palindrome_sequences import Solution


def test_solution1():
    solution = Solution()
    s = "aabca"
    expected = 3
    assert solution.countPalindromicSubsequence(s)==expected

def test_solution2():
    solution = Solution()
    s = "adc"
    expected = 0
    assert solution.countPalindromicSubsequence(s)==expected

def test_solution3():
    solution = Solution()
    s = "bbcbaba"
    expected = 4
    assert solution.countPalindromicSubsequence(s)==expected

def test_solution4():
    solution = Solution()
    s = "eokjwrihyqmotqcigqxgbxjucgsanunnmhqicczunqfqfrvfvwtlvbrasabegbvxklkikdasbtbwjnhrphyjvaeftuwhqhxzwqyawdbokocftsfxwdeqgcrobtzoqbrgfpyjrghbfmirsdovyeiusqhjrimlumcqchvxftqsxwqvptfagxordkxpwdncjagzzrtdeoowdtybtgggrnukxwbqczqhtpojjpxcgzfkviuxawlfnhdepvrkicrmpqkgdpdnxdexnkzqwsvyfpmmfkdptqnerxpbjdanxrvpexpwntcrxoayrlkwslymtjuxvolgtxcpogatannjfukclpgnopzkfooeomzpukdwdfuycnuuprbkquvmpcgjpsykrhzbuemawynfunsprjrzchkrkfasxosopjvfzlkaenonidngnugljmgiurxwmgjufsukjnsghktioeifoetyetgggfvvjudcymawywjixwohetnktdnlyajwuldniarjcjweghyielktjklozrvsuowfutmakdxqnimgwbcefgvctgjovikjrpoqnzhinulcpmywqykpkxciiqspkxuytnlewdggttfkcymbunzcqc"
    expected = 676
    assert solution.countPalindromicSubsequence(s)==expected