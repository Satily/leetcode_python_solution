class TrieNode(object):
    """
    version: Standard Release - 2018.11.7
    """
    def __init__(self, word_flag=False):
        self.next_char = {}
        self.word_flag = word_flag


class Trie(object):
    """
    version: Soltuion 648 Release - 2019.12.18
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
            if p.word_flag:
                return
        p.word_flag = True

    def prefix(self, word):
        p = self.__root        
        for i, c in enumerate(word):
            if c not in p.next_char:
                return None
            p = p.next_char[c]
            if p.word_flag:
                return word[0: i + 1]
        return None


class Solution:
    def replaceWords(self, dictionary: 'List[str]', sentence: str) -> str:
        trie = Trie()
        for word in dictionary:
            trie.insert(word)

        result = []
        for word in sentence.split(' '):
            prefix = trie.prefix(word)                
            result.append(prefix if prefix is not None else word)
        return ' '.join(result)


if __name__ == "__main__":
    print(Solution().replaceWords(["cat", "bat", "rat"], "the cattle was rattled by the battery"))
