class Solution:
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        digits.reverse()
        ld = len(digits)
        index = 0
        c = 1
        while index < ld and c == 1:
            digits[index] += c
            c, digits[index] = digits[index] // 10, digits[index] % 10
            index += 1
        if c == 1:
            digits.append(c)
        digits.reverse()
        return digits


if __name__ == "__main__":
    print(Solution().plusOne([1, 2, 3]))
    print(Solution().plusOne([4, 3, 2, 1]))
    print(Solution().plusOne([9, 9, 9]))
