from itertools import groupby


class Solution:
    def groupAnagrams(self, strs: 'List[str]') -> 'List[List[str]]':
        return [list(map(lambda x:x[1], v)) for k, v in groupby(sorted(map(lambda x: (''.join(sorted(x)), x), strs), key=lambda x: x[0]), lambda x: x[0])]


if __name__ == "__main__":
    print(Solution().groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
