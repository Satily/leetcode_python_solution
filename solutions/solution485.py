from itertools import groupby

class Solution:
    def findMaxConsecutiveOnes(self, nums: 'List[int]') -> int:
        r = list(map(lambda x: len(list(x[1])), filter(lambda x: x[0] == 1, groupby(nums))))
        return 0 if len(r) == 0 else max(r)

if __name__ == "__main__":
    print(Solution().findMaxConsecutiveOnes([0]))
    print(Solution().findMaxConsecutiveOnes([1,1,0,1,1,1]))
