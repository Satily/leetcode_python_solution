class Solution:
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        n = 0
        n_list = []
        while n ** 2 <= num:
            n_list.append(n)
            n += 1
        result = 0
        for n in reversed(n_list):
            r = result + n
            r_square = r ** 2
            if r_square == num:
                return True
            elif r_square < num:
                result = r
        return False


if __name__ == "__main__":
    print(Solution().isPerfectSquare(16))
    print(Solution().isPerfectSquare(14))
    print(Solution().isPerfectSquare(225))
