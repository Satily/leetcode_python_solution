class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        result = []
        for word in words:
            if len(word) == len(pattern):
                zipped_list = list(zip(word, pattern))
                d = {}
                for a, b in zipped_list:
                    d.setdefault(a, b)
                    if d.get(a) != b:
                        break
                else:
                    d = {}
                    for b, a in zipped_list:
                        d.setdefault(a, b)
                        if d.get(a) != b:
                            break
                    else:
                        result.append(word)
        return result


if __name__ == "__main__":
    print(Solution().findAndReplacePattern(["abc", "deq", "mee", "aqq", "dkd", "ccc"], "abb"))
    print(Solution().findAndReplacePattern(["ef", "fq", "ao", "at", "lx"], "ya"))
