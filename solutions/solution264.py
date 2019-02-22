class Solution:
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        primes, indices = [2, 3, 5], [0, 0, 0]
        ugly_numbers = [1]
        for _ in range(n):
            next_numbers = list(map(lambda x: x[0] * x[1], zip(primes, map(lambda x: ugly_numbers[x], indices))))
            min_num = min(next_numbers)
            for index in range(len(indices)):
                if next_numbers[index] == min_num:
                    indices[index] += 1
            ugly_numbers.append(min_num)
        return ugly_numbers[n - 1]


if __name__ == "__main__":
    print(Solution().nthUglyNumber(10))
    print(Solution().nthUglyNumber(11))
