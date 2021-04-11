from itertools import groupby


class Solution:
    def findAnagrams(self, s: str, p: str) -> 'List[int]':
        pdict = {k: len(list(v)) for k, v in groupby(sorted(p))}
        psum = len(p)
        start = 0
        result = []
        for ch in s:
            pdict.setdefault(ch, 0)
            pdict[ch] -= 1
            psum -= 1
            if pdict[ch] == -1:
                while pdict[ch] == -1:
                    pdict[s[start]] += 1
                    psum += 1
                    start += 1
            elif psum == 0:
                result.append(start)
                pdict[s[start]] += 1
                psum += 1
                start += 1                
        return result


if __name__ == "__main__":
    print(Solution().findAnagrams("", ""))
    print(Solution().findAnagrams("", "abc"))    
    print(Solution().findAnagrams("cbaebabacd", ""))
    print(Solution().findAnagrams("cbaebabacd", "abc"))
        