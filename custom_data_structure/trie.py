from unittest import TestCase


class TrieNode(object):
    """
    version: Standard Release - 2018.11.7
    """
    def __init__(self, word_flag=False):
        self.next_char = {}
        self.word_flag = word_flag


class Trie(object):
    """
    version: Standard Release - 2018.11.7
    """

    def __init__(self):
        self.__root = TrieNode()
        self.__word_count = 0

    def insert(self, word):
        p = self.__root
        for c in word:
            if c not in p.next_char:
                p.next_char[c] = TrieNode()
            p = p.next_char[c]
        p.word_flag = True

    def contains(self, word):
        p = self.__root
        for c in word:
            if c not in p.next_char:
                return False
            p = p.next_char[c]
        return p.word_flag

    def remove(self, word):
        raise RuntimeError("Unsupported Operation.")

    def dictionary(self):
        raise RuntimeError("Unsupported Operation.")

    def empty(self):
        raise RuntimeError("Unsupported Operation.")

    def flatten(self):
        raise RuntimeError("Unsupported Operation.")

    def __setitem__(self, key, value):
        if isinstance(value, bool):
            if value:
                self.insert(key)
            else:
                self.remove(key)
        else:
            raise RuntimeError("Type ERROR: %s." % value)

    def __getitem__(self, item):
        return self.contains(item)

    def __contains__(self, item):
        return self.contains(item)

    def __delitem__(self, key):
        self.remove(key)

    def __iter__(self):
        for word in self.dictionary():
            yield word


class TrieTest(TestCase):
    def test_insert(self):
        trie = Trie()
        trie.insert("word")
        print(trie.contains("word"))
