class Folder(object):
    def __init__(self, s):
        self.s = s

    def __iter__(self):
        if len(self.s) != 0:
            v, r = self.s[0], 1
            for c in self.s[1:]:
                if c != v:
                    yield v, r
                    v, r = c, 0
                r += 1
            yield v, r


class Solution:
    def diStringMatch(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        if len(S) == 0:
            return [0]
        if S[0] == "D":
            result = [len(S)]
            left, right = 0, len(S)
        else:
            result = [0]
            left, right = 1, len(S) + 1
        for c, r in Folder(S):
            if c == 'D':
                result.extend(reversed(range(right - r + 1, right)))
                result.append(left)
                left, right = left + 1, right - r + 1
            else:
                result.extend(range(left, left + r - 1))
                result.append(right - 1)
                left, right = left + r - 1, right - 1
        return result


if __name__ == "__main__":
    print(Solution().diStringMatch("IDID"))
    print(Solution().diStringMatch("III"))
    print(Solution().diStringMatch("DDI"))
