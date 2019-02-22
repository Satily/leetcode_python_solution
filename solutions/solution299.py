class Solution:
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        def stat(s):
            result = [0] * 10
            for c in s:
                result[int(c)] += 1
            return result

        a = len(list(filter(lambda x: x[0] == x[1], zip(secret, guess))))
        b = sum(map(min, zip(stat(secret), stat(guess)))) - a
        return "%dA%dB" % (a, b)


if __name__ == "__main__":
    print(Solution().getHint("1807", "7810"))
    print(Solution().getHint("1123", "0111"))
