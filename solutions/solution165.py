from itertools import zip_longest


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for v1n, v2n in zip_longest(map(int, version1.split('.')), map(int, version2.split('.')), fillvalue=0):
            if v1n > v2n:
                return 1
            elif v1n < v2n:
                return -1
        return 0


if __name__ == '__main__':
    print(Solution().compareVersion(version1="1.01", version2="1.001"))
    print(Solution().compareVersion(version1="1.0", version2="1.0.0"))
    print(Solution().compareVersion(version1="0.1", version2="1.1"))
    print(Solution().compareVersion(version1="1.0.1", version2="1"))
    print(Solution().compareVersion(version1="7.5.2.4", version2="7.5.3"))
