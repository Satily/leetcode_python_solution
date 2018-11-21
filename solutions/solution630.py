class Course(object):
    def __init__(self, course):
        self.last_start_day = course[1] - course[0]
        self.duration = course[0]


class Solution:
    def scheduleCourse(self, courses):
        """
        :type courses: List[List[int]]
        :rtype: int
        """
        c = sorted(map(lambda x: Course(x), courses), key=lambda x: x.last_start_day)
        return c


if __name__ == "__main__":
    print(Solution().scheduleCourse([[100, 200], [200, 1300], [1000, 1250], [2000, 3200]]))
