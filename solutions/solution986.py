from data_structure import Interval, flatten_interval


class Solution:
    def intervalIntersection(self, A: 'List[Interval]', B: 'List[Interval]') -> 'List[Interval]':
        ia, ib = 0, 0
        result = []
        while ia < len(A) and ib < len(B):
            a, b = A[ia], B[ib]
            s, e = max(a.start, b.start), min(a.end, b.end)
            if s <= e:
                result.append(Interval(s, e))
            if a.end < b.end:
                ia += 1
            else:
                ib += 1
        return result


if __name__ == '__main__':
    result = Solution().intervalIntersection([
        Interval(0, 2),
        Interval(5, 10),
        Interval(13, 23),
        Interval(24, 25)
    ], [
        Interval(1, 5),
        Interval(8, 12),
        Interval(15, 24),
        Interval(25, 26)
    ])
    print(list(map(flatten_interval, result)))
