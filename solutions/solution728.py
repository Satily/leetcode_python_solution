class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> 'List[int]':
        result = []
        for num in range(left, right + 1):
            num2 = num
            flag = True
            while num2 > 0:
                digit = num2 % 10
                num2 //= 10
                if digit == 0 or num % digit != 0:
                    flag = False
                    break
            if flag:
                result.append(num)
        return result


if __name__ == "__main__":
    print(Solution().selfDividingNumbers(1, 22))
