from itertools import groupby


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        pdict = {k: len(list(v)) for k, v in groupby(sorted(s1))}
        psum = len(s1)
        start = 0
        for ch in s2:
            pdict.setdefault(ch, 0)
            pdict[ch] -= 1
            psum -= 1
            if pdict[ch] == -1:
                while pdict[ch] == -1:
                    pdict[s2[start]] += 1
                    psum += 1
                    start += 1
            elif psum == 0:
                return True                
        return False


if __name__ == "__main__":
    print(Solution().checkInclusion(s1 = "ab", s2 = "eidbaooo"))
    print(Solution().checkInclusion(s1= "ab", s2 = "eidboaoo"))