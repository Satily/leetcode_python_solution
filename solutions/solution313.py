class Solution:
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        indices = [0] * len(primes)
        ugly_numbers = [1]
        next_numbers = primes.copy()
        for _ in range(n):
            min_num = min(next_numbers)
            ugly_numbers.append(min_num)
            for index in range(len(indices)):
                if next_numbers[index] == min_num:
                    indices[index] += 1
                    next_numbers[index] = primes[index] * ugly_numbers[indices[index]]
        return ugly_numbers[n - 1]


if __name__ == "__main__":
    print(Solution().nthSuperUglyNumber(12, [2, 7, 13, 19]))
    print(Solution().nthSuperUglyNumber(100000,
                                        [7, 19, 29, 37, 41, 47, 53, 59, 61, 79, 83, 89, 101, 103, 109, 127, 131, 137,
                                         139, 157, 167, 179, 181, 199, 211, 229, 233, 239, 241, 251]))
