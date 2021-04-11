class TrieNode(object):
    """
    version: Standard Release - 2018.11.7
    """

    def __init__(self, word_flag=False):
        self.next_char = {}
        self.word_flag = word_flag


class Trie(object):
    """
    version: Solution 211 Release - 2018.12.3
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

    def contains_with_dot(self, word):
        return self.__contains_with_dot_helper(self.__root, word, 0)

    def __contains_with_dot_helper(self, node, word, index):
        if index == len(word):
            return node.word_flag
        elif word[index] == '.':
            for key, value in node.next_char.items():
                if self.__contains_with_dot_helper(value, word, index + 1):
                    return True
            return False
        else:
            if word[index] in node.next_char:
                return self.__contains_with_dot_helper(node.next_char[word[index]], word, index + 1)
            else:
                return False


class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.trie = Trie()

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        self.trie.insert(word)

    def search(self, word):
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        return self.trie.contains_with_dot(word)


if __name__ == "__main__":
    word_dictionary = WordDictionary()
    word_dictionary.addWord("bad")
    word_dictionary.addWord("dad")
    word_dictionary.addWord("mad")
    print(word_dictionary.search("pad"))  # false
    print(word_dictionary.search("bad"))  # true
    print(word_dictionary.search(".ad"))  # true
    print(word_dictionary.search("b.."))  # true
