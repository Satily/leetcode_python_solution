class Solution:
    def fizzBuzz(self, n: int) -> 'List[str]':
        result = []
        for i in range(1, n + 1):
            if i % 15 == 0:
                ele = "FizzBuzz"
            elif i % 3 == 0:
                ele = "Fizz"
            elif i % 5 == 0:
                ele = "Buzz"
            else:
                ele = str(i)
            result.append(ele)
        return result


if __name__ == "__main__":
    print(Solution().fizzBuzz(15))