class Solution:
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        lines = list(map(lambda x: set(x), ["qwertyuiop", "asdfghjkl", "zxcvbnm"]))
        return [word for word in words if sum([sum([ch in line for ch in word.lower()]) == len(word) for line in lines]) == 1]


if __name__ == "__main__":
    print(Solution().findWords(["Hello", "Alaska", "Dad", "Peace"]))
