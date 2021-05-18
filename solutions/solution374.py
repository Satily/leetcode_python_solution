pick = 0


def guess(num: int) -> int:
    if pick < num:
        return -1
    elif pick == num:
        return 0
    else:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left, right = 1, n
        while left < right:
            mid = (left + right) >> 1
            guess_result = guess(mid)
            if guess_result < 0:
                right = mid - 1
            elif guess_result > 0:
                left = mid + 1
            else:
                return mid
        return left


if __name__ == '__main__':
    pick = 6
    print(Solution().guessNumber(10))
    pick = 1
    print(Solution().guessNumber(1))
    pick = 1
    print(Solution().guessNumber(2))
    pick = 2
    print(Solution().guessNumber(2))