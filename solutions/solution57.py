from data_structure import Interval, flatten_interval


class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """
        result = []
        for index, interval in enumerate(intervals):
            if newInterval is not None and newInterval.end < interval.start:
                result.append(newInterval)
                newInterval = None
            if newInterval is not None and (interval.end - interval.start) + (newInterval.end - newInterval.start) >= max(newInterval.end, interval.end) - min(newInterval.start, interval.start):
                newInterval.start, newInterval.end = min(interval.start, newInterval.start), max(interval.end, newInterval.end)
            else:
                result.append(interval)
        if newInterval is not None:
            result.append(newInterval)
        return result


def interval_print(interval_list):
    print(*list(map(flatten_interval, interval_list)))


if __name__ == "__main__":
    interval_print(Solution().insert([Interval(1, 5)], Interval(2, 3)))
    interval_print(Solution().insert([Interval(1, 3), Interval(6, 9)], Interval(2, 5)))
    interval_print(Solution().insert([Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)], Interval(4, 8)))
    interval_print(Solution().insert([Interval(3, 5), Interval(6, 7), Interval(8, 10), Interval(12, 16)], Interval(1, 2)))
    interval_print(Solution().insert([Interval(1, 2), Interval(3, 5), Interval(6, 7), Interval(8, 10)], Interval(12, 16)))
    interval_print(Solution().insert([], Interval(12, 16)))
