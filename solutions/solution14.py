class Solution:
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        if len(strs) == 0:
            return ''
        # find shortest
        min_len = len(strs[0])
        min_len_index = 0
        for i, s in enumerate(strs):
            if len(s) < min_len:
                min_len = len(s)
                min_len_index = i
        # swap it to first
        t = strs[0]
        strs[0] = strs[min_len_index]
        strs[min_len_index] = t
        # find prefix
        for i in range(0, min_len):
            o = strs[0][i]
            for j in range(1, len(strs)):
                if o != strs[j][i]:
                    return strs[0][0: i]
        return strs[0]


if __name__ == "__main__":
    print(Solution().longestCommonPrefix(["aa", "a"]))
    print(Solution().longestCommonPrefix(["flower", "flow", "flight"]))
    print(Solution().longestCommonPrefix(["dog", "racecar", "car"]))
    print(Solution().longestCommonPrefix(["dog", "dog", "dog"]))
