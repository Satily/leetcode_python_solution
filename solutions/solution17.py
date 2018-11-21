class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if digits == "":
            return []
        digits_dict = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz',
        }
        result = [""]
        for digit in digits:
            temp_result = []
            for r in result:
                for alpha in digits_dict[digit]:
                    temp_result.append(r + alpha)
            result = temp_result
        return result


if __name__ == "__main__":
    print(Solution().letterCombinations("23"))
