import random


class Solution:
    def __init__(self, radius: 'float', x_center: 'float', y_center: 'float'):
        self.radius = radius
        self.x_center = x_center
        self.y_center = y_center

    def randPoint(self) -> 'List[float]':
        x, y = -self.radius, -self.radius
        while x ** 2 + y ** 2 >= self.radius ** 2:
            x, y = random.uniform(-self.radius, self.radius), random.uniform(-self.radius, self.radius)
        return [self.x_center + x, self.y_center + y]


if __name__ == "__main__":
    print(Solution(1, 0, 0).randPoint())
