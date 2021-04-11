class Solution:
    def countBits(self, num: int) -> 'List[int]':
        result = [0]
        while len(result) <= num:
            lr = len(result)
            for index in range(lr):
                result.append(result[index] + 1)
                if len(result) > num:
                    break
        return result


if __name__ == "__main__":
    print(Solution().countBits(0))
    print(Solution().countBits(2))
    print(Solution().countBits(5))
