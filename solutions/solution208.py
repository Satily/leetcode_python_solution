class TrieNode(object):
    """
    version: Standard Release - 2018.11.7
    """
    def __init__(self, word_flag=False):
        self.next_char = {}
        self.word_flag = word_flag


class Trie:
    """
    version: Solution 208 Release - 2018.11.7
    """
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.__root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        p = self.__root
        for c in word:
            if c not in p.next_char:
                p.next_char[c] = TrieNode()
            p = p.next_char[c]
        p.word_flag = True

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        p = self.__root
        for c in word:
            if c not in p.next_char:
                return False
            p = p.next_char[c]
        return p.word_flag

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        p = self.__root
        for c in prefix:
            if c not in p.next_char:
                return False
            p = p.next_char[c]
        return p is not None


if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
    print(trie.startsWith("apb"))
