from itertools import groupby
from copy import deepcopy


class Solution:
    def subsetsWithDup(self, nums: 'List[int]') -> 'List[List[int]]':
        def dfs(num_list, current, deep, result):
            if deep == len(num_list):
                result.append(deepcopy(current))
                return
            num, count = num_list[deep]
            for i in range(count + 1):
                if i != 0:
                    current.append(num)
                dfs(num_list, current, deep + 1, result)
            for i in range(count):
                current.pop()
                
        nums2 = list(map(lambda x: (x[0], len(list(x[1]))), groupby(sorted(nums))))
        result = []
        dfs(nums2, [], 0, result)
        return result        


if __name__ == "__main__":
    print(Solution().subsetsWithDup([1,2,2]))