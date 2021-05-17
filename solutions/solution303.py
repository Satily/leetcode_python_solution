class NumArray:
    def __init__(self, nums: 'List[int]'):
        self.sums = [0]
        for num in nums:
            self.sums.append(self.sums[-1] + num)

    def sumRange(self, i: int, j: int) -> int:
        return self.sums[j + 1] - self.sums[i]


if __name__ == '__main__':
    num_array = NumArray([-2, 0, 3, -5, 2, -1])
    print(num_array.sumRange(0, 2))
    print(num_array.sumRange(2, 5))
    print(num_array.sumRange(0, 5))

