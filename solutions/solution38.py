class Solution:
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        def next_str(s):
            last = s[0]
            last_count = 1
            r = ''
            for i in range(1, len(s)):
                if s[i] != last:
                    r += str(last_count) + str(last)
                    last, last_count = s[i], 1
                else:
                    last_count += 1
            r += str(last_count) + str(last)
            return r

        result = '1'
        for _ in range(n - 1):
            result = next_str(result)
        return result


if __name__ == "__main__":
    # print(Solution().countAndSay(1))
    print(Solution().countAndSay(4))
