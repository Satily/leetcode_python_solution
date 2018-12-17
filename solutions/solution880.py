class Item(object):
    def __init__(self, string, times):
        self.times = times
        self.string = string
        self.single_length = 0
        self.length = 0


class Parser(object):
    def __init__(self, s):
        self.s = s

    def __iter__(self):
        rs = ''
        num_set = set(map(str, range(10)))
        for ch in self.s:
            if ch in num_set:
                yield Item(rs, int(ch))
                rs = ''
            else:
                rs += ch
        if rs != '':
            yield Item(rs, 1)


class Solution:
    def decodeAtIndex(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """
        K -= 1
        items = list(Parser(S))
        s = 0
        for item in items:
            item.single_length = s + len(item.string)
            item.length = s = item.single_length * item.times
        last = 0
        while items[last].length <= K:
            last += 1
        for index, item in enumerate(reversed(items[:last + 1])):
            K %= item.single_length
            if item.single_length - K <= len(item.string):
                return item.string[len(item.string) - item.single_length + K]


if __name__ == "__main__":
    print(Solution().decodeAtIndex("a2b3c4d5e6f7g8h9", 3))
    print(Solution().decodeAtIndex("leet2code3", 10))
    print(Solution().decodeAtIndex("ha22", 5))
    print(Solution().decodeAtIndex("a2345678999999999999999", 1))
