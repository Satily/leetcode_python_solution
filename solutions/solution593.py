class Vector(object):
    def __init__(self, p0, p1):
        self.x = p1[0] - p0[0]
        self.y = p1[1] - p0[1]

    def is_vertical(self, other):
        return not self.dot(other)

    def dot(self, other):
        return self.x * other.x + self.y * other.y

    def norm_square(self):
        return self.dot(self)


class Solution:
    def validSquare(self, p1, p2, p3, p4):
        """
        :type p1: List[int]
        :type p2: List[int]
        :type p3: List[int]
        :type p4: List[int]
        :rtype: bool
        """
        points = [p1, p2, p3, p4]
        for i in range(1, len(points)):
            vi = Vector(points[0], points[i])
            for j in range(i + 1, len(points)):
                vj = Vector(points[0], points[j])
                if vi.is_vertical(vj) and vi.norm_square() == vj.norm_square() != 0:
                    k = 6 - i - j
                    vik = Vector(points[i], points[k])
                    vjk = Vector(points[j], points[k])
                    if vi.is_vertical(vik) and vj.is_vertical(vjk) and vik.is_vertical(vjk):
                        return True
        return False


if __name__ == "__main__":
    print(Solution().validSquare([0, 0], [5, 0], [5, 4], [0, 4]))
    print(Solution().validSquare([0, 0], [2, 1], [1, 0], [0, 1]))
