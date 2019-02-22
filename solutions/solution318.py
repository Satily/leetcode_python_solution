from itertools import product


class Solution:
    def maxProduct(self, words: 'List[str]') -> 'int':
        word_vectors = [(len(word), sum({1 << (ord(ch) - 97) for ch in word})) for word in words]
        result = max([l0 * l1 for (l0, o0), (l1, o1) in product(word_vectors, word_vectors) if o0 & o1 == 0] + [0])
        return result


if __name__ == "__main__":
    print(Solution().maxProduct(["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]))
    print(Solution().maxProduct(["a", "ab", "abc", "d", "cd", "bcd", "abcd"]))
    print(Solution().maxProduct(["a", "aa", "aaa", "aaaa"]))
