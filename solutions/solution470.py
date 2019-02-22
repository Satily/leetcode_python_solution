import random
import math


def rand7():
    return math.floor(random.uniform(1, 8))


class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        r = 343
        while r >= 340:
            r = rand7() * 49 + rand7() * 7 + rand7() - 57
        return r % 10 + 1


if __name__ == '__main__':
    print(Solution().rand10())
