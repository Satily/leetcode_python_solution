class TrieNode(object):
    """
    version: Solution 677 Release - 2019.2.26
    """
    def __init__(self, weight = 0):
        self.next_char = {}
        self.weight = weight


class Trie(object):
    """
    version: Solution 677 Release - 2019.2.26
    """
    def __init__(self):
        self.__root = TrieNode()

    def insert(self, word, weight):
        p = self.__root
        p.weight += weight
        for c in word:
            if c not in p.next_char:
                p.next_char[c] = TrieNode()
            p = p.next_char[c]
            p.weight += weight

    def search(self, word):
        p = self.__root
        for c in word:
            if c not in p.next_char:
                return 0
            p = p.next_char[c]
        return p.weight


class MapSum:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()
        self.dictionary = {}

    def insert(self, key: str, val: int) -> None:
        obj = val
        if key in self.dictionary:
            obj -= self.dictionary[key]
        self.dictionary[key] = val
        self.trie.insert(key, obj)

    def sum(self, prefix: str) -> int:
        return self.trie.search(prefix)


if __name__ == '__main__':
    mapSum = MapSum()
    mapSum.insert("apple", 3)
    print(mapSum.sum("ap"))
    mapSum.insert("app", 2)
    print(mapSum.sum("ap"))

    mapSum = MapSum()
    mapSum.insert("aa", 3)
    print(mapSum.sum("a"))
    mapSum.insert("aa", 2)
    print(mapSum.sum("a"))
