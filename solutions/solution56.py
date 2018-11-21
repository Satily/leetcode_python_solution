from data_structure import Interval, flatten_interval


class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        if len(intervals) == 0:
            return []
        intervals.sort(key=lambda x: (x.start, x.end))
        item = Interval(intervals[0].start, intervals[0].end)
        result = []
        for i in range(1, len(intervals)):
            current = intervals[i]
            if item.end >= current.start:
                item.end = max(item.end, current.end)
            else:
                result.append(item)
                item = Interval(intervals[i].start, intervals[i].end)
        result.append(item)
        return result


def interval_print(interval_list):
    print(*list(map(flatten_interval, interval_list)))


if __name__ == "__main__":
    interval_print(Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]))
    interval_print(Solution().merge([Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]))
    interval_print(Solution().merge([Interval(1, 4), Interval(4, 5)]))
