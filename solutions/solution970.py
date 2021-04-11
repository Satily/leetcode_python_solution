class Solution:
    def powerfulIntegers(self, x, y, bound):
        """
        :type x: int
        :type y: int
        :type bound: int
        :rtype: List[int]
        """
        def powers(n, bound):
            if n == 1:
                return [1]
            power_list = []
            s = 1
            while s <= bound:
                power_list.append(s)
                s *= n
            return power_list

        result = set()
        x_powers = powers(x, bound)
        y_powers = powers(y, bound)
        for x_power in x_powers:
            for y_power in y_powers:
                if x_power + y_power <= bound:
                    result.add(x_power + y_power)
        return list(result)



if __name__ == "__main__":
    print(Solution().powerfulIntegers(2, 3, 10))
    print(Solution().powerfulIntegers(3, 5, 15))
    print(Solution().powerfulIntegers(1, 2, 100))
