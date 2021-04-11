from itertools import groupby


class Solution:
    def minimumSwap(self, s1: str, s2: str) -> int:
        r = {key : len(list(value)) for key, value in groupby(
                sorted(
                    filter(
                        lambda x: x == 1 or x == -1, 
                        map(
                            lambda x: 0 if x[0] == x[1] else (1 if x[0] == 'x' else -1), 
                            zip(s1, s2)
                        )
                    )
                )
            )
        }
        r.setdefault(-1, 0)
        r.setdefault(1, 0)
        return -1 if (r[-1] + r[1]) & 1 == 1 else (r[-1] >> 1) + (r[1] >> 1) + ((r[-1] & 1) << 1)
                

        

if __name__ == "__main__":
    print(Solution().minimumSwap("xx", "yy"))
    print(Solution().minimumSwap("xy", "yx"))
    print(Solution().minimumSwap("xx", "xy"))
    print(Solution().minimumSwap("xxyyxyxyxx", "xyyxyxxxyx"))
