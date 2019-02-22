class Solution:
    def shiftingLetters(self, S, shifts):
        """
        :type S: str
        :type shifts: List[int]
        :rtype: str
        """
        a = ord("a")
        s = 0
        result = ""
        for index in reversed(range(len(shifts))):
            s += shifts[index]
            s %= 26
            result = chr((ord(S[index]) - a + s) % 26 + a) + result
        return result


if __name__ == "__main__":
    print(Solution().shiftingLetters("abc", [3, 5, 9]))
